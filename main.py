import json
import os
import sys
import requests
import sqlite3
import base64

from lxml import etree
from lxml.etree import _ElementTree, ElementBase
from io import StringIO
from urllib.parse import urlparse
from typing import List, Tuple

import proto_pb2 as proto

HTML_PARSER = etree.HTMLParser()

class FavoritedGIF:

    def __init__(self, data: dict) -> None:
        self.w = data["width"]
        self.h = data["height"]
        self.src: str = data["src"]
        self.url: str = data["url"]
        self.format = data["format"]
        self.path: str = data.get("path", None)

    @property
    def url_host(self):
        return urlparse(self.url).hostname

    @property
    def sanitized_url(self):
        url_comps = urlparse(self.url)
        # If URL ends with an extension, it's safe to assume that parameters would not be useful
        if url_comps.path.endswith(".gif"):
            return f"{url_comps.scheme}://{url_comps.netloc}{url_comps.path}"
        return self.url

    def serialize(self) -> dict:
        return {
            "width": self.w,
            "height": self.h,
            "src": self.src,
            "url": self.url,
            "format": self.format,
            "path": self.path
        }

    def _download_generic(self, url):
        # Create downloads path if it doesn't exist
        if not os.path.exists("downloads"):
            os.mkdir("downloads")

        file_name = os.path.basename(url)
        file_path = os.path.join("downloads", file_name)

        # Create file and make sure it doesn't duplicate
        i = 1
        name, extension = os.path.splitext(file_name)
        while os.path.exists(file_path):
            file_path = os.path.join("downloads", name + "-" + str(i) + extension)
            i += 1

        # Download the file
        r = requests.get(url)
        with open(file_path, mode="wb") as f:
            f.write(r.content)

        self.path = file_path

        print(f"[DOWNLOAD] {self.sanitized_url}")

    def _extract_tenor_url(self, url):
        r = requests.get(url)
        tree: _ElementTree = etree.parse(StringIO(r.text), HTML_PARSER)
        meta_tags: List[ElementBase] = tree.xpath("//meta")
        for tag in meta_tags:
            if "itemprop" in tag.attrib:
                if tag.attrib["itemprop"] == 'contentUrl':
                    return tag.attrib["content"]

    def download(self):
        if self.path is not None:
            return

        # If URL ends with .gif, it's very likely it's a plain file
        if self.sanitized_url.endswith(".gif"):
            return self._download_generic(self.sanitized_url)

        # Handle tenor URLs
        if self.url_host == "tenor.com":
            url = self._extract_tenor_url(self.sanitized_url)
            # Edge case where tenor gifs get removed
            if url is not None:
                return self._download_generic(url)
            return None

        else:
            print()
            print(f"[UNSUPPORTED URL] ({self.url_host})", self.sanitized_url)
            print()

class DataNotLoadedError(Exception):
    def __init__(self) -> None:
        super().__init__("Data has not been loaded")

class DataManager:

    def __init__(self, load: bool = True) -> None:
        self._gif_list: List[dict] = None

        if load:
            self.load()

    @property
    def data(self):
        if self._gif_list is None:
            raise DataNotLoadedError
        return self._gif_list

    def load(self) -> bool:
        """Loads data from file to memory."""
        # If data file does not exist, sets the value to empty dict and returns false
        if not os.path.exists("data.json"):
            self._gif_list = []
            return False

        # If data file exists, load it
        with open("data.json", mode="r") as f:
            self._gif_list = json.load(f)
        return True

    def save(self) -> None:
        """Saves data from memory to file."""
        with open("data.json", mode="w") as f:
            json.dump(self._gif_list, f)

    def merge(self, new_gif_list: List[dict]):
        """Merges 2 lists together.

        Note, this does not remove the old entries."""

        # If no data was loaded, just pass the new gif list and be done with it.
        if self._gif_list is None or len(self._gif_list) == 0:

            # Avoid duplicate entries upon initial load
            temp_gif_urls = []
            for i, gif in enumerate(new_gif_list):
                if gif["url"] in temp_gif_urls:
                    new_gif_list.pop(i)
                    continue
                temp_gif_urls.append(gif["url"])

            self._gif_list = new_gif_list
            return self.data

        orig_url_list = []
        for gif in self._gif_list:
            orig_url_list.append(gif["url"])

        for gif in new_gif_list:
            if gif["url"] in orig_url_list:
                continue

            print("[MERGE]", gif["url"])
            self._gif_list.append(gif)

    def deserialize_gifs(self) -> List[FavoritedGIF]:
        """Deserializes and returns a list of FavoritedGIF objects."""
        return [FavoritedGIF(d) for d in self._gif_list]

    def serialize_gifs(self, gifs: List[FavoritedGIF]) -> List[dict]:
        """Serializes and returns a list of GIF dicts."""
        self._gif_list = [gif.serialize() for gif in gifs]
        return self.data


class LocalStorageEntry:

    def __init__(self, data: Tuple[str, str, str]) -> None:
        self.origin_attributes, self.key, self.value = data

class ProtoSettingsReader:

    def __init__(self, raw_string: str) -> None:
        decoded_bytes = base64.decodebytes(bytes(raw_string, encoding="utf-8"))
        self._proto = proto.FrecencyUserSettings()
        self._proto.ParseFromString(decoded_bytes)

    def get_versions(self):
        return self._proto.versions

    # Why is this the only one that returns civilized data?
    # The only reason for is because I actually need to use and parse
    # this data. Other methods exist just so I can do the pro-grammer
    # move of just copy pasting this class in my other projects,
    # just in case I ever need it :)
    def get_favorite_gifs(self) -> List[dict]:
        """Returns a dictionary list of favorite gifs.
        Note: list is not guaranteed to be in the same order every time."""
        gifs = []
        for key in self._proto.favorite_gifs.gifs:
            # We will not be taking advantage of GIF order
            mapping = self._proto.favorite_gifs.gifs[key]
            gif_dict = {
                "width": mapping.width,
                "height": mapping.height,
                "src": mapping.src,
                "url": key,
                "format": "VIDEO" if mapping.format == 2 else "IMAGE"
            }
            gifs.append(gif_dict)
        return gifs

    def get_favorite_stickers(self):
        return self._proto.favorite_stickers

    def get_sticker_frecency(self):
        return self._proto.sticker_frecency

    def get_favorite_emojis(self):
        return self._proto.favorite_emojis

    def get_emoji_frecency(self):
        return self._proto.emoji_frecency

    def get_application_command_frecency(self):
        return self._proto.application_command_frecency


def main():
    if len(sys.argv) > 2:
        print("Too many args passed. If you want to fetch proto-settings, please pass your discord token")
        exit(1)

    fetch_proto_settings = len(sys.argv) == 2

    # Initial value
    manager = DataManager()
    gifs = []

    # Fetch data from new API
    if fetch_proto_settings:
        r = requests.get("https://discord.com/api/v9/users/@me/settings-proto/2", headers={
            "Authorization": sys.argv[1]
        })
        data = r.json()
        if "settings" not in data:
            print("Tried using token, but an error was encountered:", data["message"])
            exit(100)

        reader = ProtoSettingsReader(data["settings"])
        manager.merge(reader.get_favorite_gifs())

    # Use old school method
    else:

        # This is all purely for my use case, it uses Mozilla's localstorage DB
        db = sqlite3.connect(
            os.path.join(os.getenv('APPDATA'), "Mozilla\\Firefox\\Profiles\\lv99cc5z.default-release\\webappsstore.sqlite")
        )
        cur = db.cursor()
        cur.execute(
            "SELECT originattributes, key, value "
            "FROM webappsstore2 "
            "WHERE originattributes LIKE '%firstPartyDomain=discord.com' AND `key` = 'GIFFavoritesStore'"
        )
        entries = [LocalStorageEntry(t) for t in cur.fetchall()]

        for entry in entries:

            # Get the correct item, userContextId=1 is from containers, this one refers to my personal one
            if 'userContextId=1' in entry.origin_attributes:
                data = json.loads(entry.value)
                manager.merge(data["_state"]["favorites"])
                break

    gifs = manager.deserialize_gifs()
    if len(gifs) == 0:
        print("Failure: no GIFs were deserialized!")
        exit(2)

    for gif in gifs:
        gif.download()

    manager.serialize_gifs(gifs)
    manager.save()


if __name__ == "__main__":
    main()
