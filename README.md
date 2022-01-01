# Discord-favourite-GIF-downloader
Downloads your favourited GIFs on Discord.

## How to use

To create a protobuf file, run the following command.
Protobuf compiler is provided together with the repo for convenience. The original file can be found [here](https://github.com/protocolbuffers/protobuf/releases/latest).
```sh
protoc -I=. --python_out=. ./proto.proto
```

To use the said protobuf file, you'll also need to install the protobuf dependency.
```sh
python -m pip install protobuf
```
