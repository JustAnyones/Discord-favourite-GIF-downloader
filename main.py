
import json
import argparse
import os
import requests # type: ignore
import base64

from lxml import etree # type: ignore
from lxml.etree import _ElementTree, ElementBase # type: ignore
from io import StringIO
from urllib.parse import urlparse
from typing import Any

import proto_pb2 as proto

HTML_PARSER = etree.HTMLParser()

class FavoritedGIF:

    def __init__(self, data: dict[str, Any]) -> None:
        self.w: int = data["width"]
        self.h: int = data["height"]
        self.src: str = data["src"]
        self.url: str = data["url"]
        self.format: str = data["format"]
        self.path: str | None = data.get("path", None)
        self.refreshed_url: str | None = data.get("refreshed_url", None)

    @property
    def url_host(self):
        return urlparse(self.url).hostname

    @property
    def sanitized_url(self):
        url = self.url
        if self.refreshed_url is not None:
            url = self.url
        url_comps = urlparse(url)
        # If URL ends with an extension, it's safe to assume that parameters would not be useful
        if url_comps.path.endswith(".gif"):
            return f"{url_comps.scheme}://{url_comps.netloc}{url_comps.path}"
        return url

    def serialize(self) -> dict[str, Any]:
        return {
            "width": self.w,
            "height": self.h,
            "src": self.src,
            "url": self.url,
            "format": self.format,
            "path": self.path,
            "refreshed_url": self.refreshed_url
        }

    def _download_generic(self, url: str):
        # Create downloads path if it doesn't exist
        if not os.path.exists("downloads"):
            os.mkdir("downloads")

        file_name = os.path.basename(self.sanitized_url)
        file_path = os.path.join("downloads", file_name)

        # Create file and make sure it doesn't duplicate
        i = 1
        name, extension = os.path.splitext(file_name)
        while os.path.exists(file_path):
            file_path = os.path.join("downloads", name + "-" + str(i) + extension)
            i += 1

        # Download the file
        try:
            r = requests.get(url)
            with open(file_path, mode="wb") as f:
                _ = f.write(r.content)
            r.raise_for_status()
        except Exception as e:
            print(f"[ERROR] Failed to download {url}: {e}")
            # remove the partially created file
            if os.path.exists(file_path):
                os.remove(file_path)
            return

        self.path = file_path
        print(f"[DOWNLOADED] {url} (status: {r.status_code}) -> {self.path}")

    def _extract_tenor_url(self, url: str) -> str:
        r = requests.get(url)
        tree: _ElementTree = etree.parse(StringIO(r.text), HTML_PARSER)
        meta_tags: list[ElementBase] = tree.xpath("//meta")
        for tag in meta_tags:
            if "itemprop" in tag.attrib:
                if tag.attrib["itemprop"] == 'contentUrl':
                    return tag.attrib["content"]

    def download(self):
        if self.path is not None:
            return

        url = self.refreshed_url or self.url

        # If URL ends with .gif, it's very likely it's a plain file
        if os.path.basename(self.sanitized_url).endswith(".gif"):
            return self._download_generic(url)

        # Handle tenor URLs
        if self.url_host == "tenor.com":
            url = self._extract_tenor_url(url)
            # Edge case where tenor gifs get removed
            if url is not None:
                return self._download_generic(url)
            return None

        else:
            print()
            print(f"[UNSUPPORTED URL] ({self.url_host})", url)
            print()

class DataNotLoadedError(RuntimeError):
    def __init__(self) -> None:
        super().__init__("Data has not been loaded")

class DataManager:

    def __init__(self, load: bool = True) -> None:
        self._gif_list: list[dict] | None = None

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

    def merge(self, new_gif_list: list[dict]):
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

    def deserialize_gifs(self) -> list[FavoritedGIF]:
        """Deserializes and returns a list of FavoritedGIF objects."""
        return [FavoritedGIF(d) for d in self._gif_list or []]

    def serialize_gifs(self, gifs: list[FavoritedGIF]) -> list[dict]:
        """Serializes and returns a list of GIF dicts."""
        self._gif_list = [gif.serialize() for gif in gifs]
        return self.data


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
    def get_favorite_gifs(self) -> list[dict]:
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
                "format": "VIDEO" if mapping.format == 2 else "IMAGE",
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
    parser = argparse.ArgumentParser("Discord favourite GIF downloader")
    parser.add_argument("-t", "--token", help="Specifies Discord token", required=True)
    args = parser.parse_args()
    
    # Initialize some managers and stuff
    manager = DataManager()
    gifs = []


    print("Acquiring data from the API")
    token: str = args.token

    # Fetch data from new API
    r = requests.get("https://discord.com/api/v9/users/@me/settings-proto/2", headers={
        "Authorization": token
    })
    data: dict[str, Any] = r.json()
    if "settings" not in data:
        raise RuntimeError(f"Tried using token, but an error was encountered:\n{data['message']}")

    reader = ProtoSettingsReader(data["settings"])
    manager.merge(reader.get_favorite_gifs())
    

    # Do the actual data clean-up
    gifs = manager.deserialize_gifs()
    if len(gifs) == 0:
        print("Failure: no GIFs were deserialized!")
        exit(2)

    urls_to_refresh: list[tuple[int, str]] = []
    for i, gif in enumerate(gifs):
        if ("media.discordapp.net" in (gif.url_host or "discord") \
            or "cdn.discordapp.net" in (gif.url_host or "discord"))\
            and gif.refreshed_url is None:
            print("[SKIP DISCORD GIF]", gif.url, gif.refreshed_url)
            urls_to_refresh.append((i, gif.url))
            continue
        try:
            gif.download()
        except Exception as e:
            print(f"[ERROR] Failed to download {gif.sanitized_url}: {e}")


    # Refresh Discord URLs
    refreshed_urls: list[tuple[int, str]] = []
    for i in range(0, len(urls_to_refresh), 50):
        batch = urls_to_refresh[i:i+50]
        r = requests.post(
            "https://discord.com/api/v9/attachments/refresh-urls",
            json={
                "attachment_urls": [url for _, url in batch]
            },
            headers={
                "Authorization": token,
                "Content-Type": "application/json"
            }
        )
        if r.status_code != 200:
            print(f"[ERROR] Failed to refresh URL batch starting at index {i}: {r.status_code} {r.text}")
            continue
        resp_json = r.json()
        for j, refreshed_url in enumerate(resp_json["refreshed_urls"]):
            refreshed_urls.append((batch[j][0], refreshed_url["refreshed"]))
    # Apply refreshed URLs
    for index, new_url in refreshed_urls:
        gifs[index].refreshed_url = new_url
    print(f"{len(refreshed_urls)} URLs refreshed.")

    manager.serialize_gifs(gifs)
    manager.save()


if __name__ == "__main__":
    main()
