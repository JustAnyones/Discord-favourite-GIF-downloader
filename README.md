# Discord-favourite-GIF-downloader
Downloads your favourited GIFs on Discord.

## Running
You need Astral UV. You can run the script like so:
```sh
uv run main.py -t YOUR_TOKEN
```

## Protobuf file generation

A generated protobuf file is provided for convenience.

To create a protobuf file, run the following command.
~~Protobuf compiler is provided together with the repo for convenience. The original file can be found [here](https://github.com/protocolbuffers/protobuf/releases/latest).~~ 
```sh
protoc -I=. --python_out=. ./proto.proto
```
