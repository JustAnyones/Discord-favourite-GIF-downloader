# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bproto.proto\x12\x07\x64iscord\"X\n\x0c\x46recencyItem\x12\x12\n\ntotal_uses\x18\x01 \x01(\r\x12\x13\n\x0brecent_uses\x18\x02 \x03(\x04\x12\x10\n\x08\x66recency\x18\x03 \x01(\x05\x12\r\n\x05score\x18\x04 \x01(\x05\"\xf5\x0c\n\x14\x46recencyUserSettings\x12\x38\n\x08versions\x18\x01 \x01(\x0b\x32&.discord.FrecencyUserSettings.Versions\x12\x41\n\rfavorite_gifs\x18\x02 \x01(\x0b\x32*.discord.FrecencyUserSettings.FavoriteGIFs\x12I\n\x11\x66\x61vorite_stickers\x18\x03 \x01(\x0b\x32..discord.FrecencyUserSettings.FavoriteStickers\x12G\n\x10sticker_frecency\x18\x04 \x01(\x0b\x32-.discord.FrecencyUserSettings.StickerFrecency\x12\x45\n\x0f\x66\x61vorite_emojis\x18\x05 \x01(\x0b\x32,.discord.FrecencyUserSettings.FavoriteEmojis\x12\x43\n\x0e\x65moji_frecency\x18\x06 \x01(\x0b\x32+.discord.FrecencyUserSettings.EmojiFrecency\x12^\n\x1c\x61pplication_command_frecency\x18\x07 \x01(\x0b\x32\x38.discord.FrecencyUserSettings.ApplicationCommandFrecency\x1aP\n\x08Versions\x12\x16\n\x0e\x63lient_version\x18\x01 \x01(\r\x12\x16\n\x0eserver_version\x18\x02 \x01(\r\x12\x14\n\x0c\x64\x61ta_version\x18\x03 \x01(\r\x1a\x93\x03\n\x0c\x46\x61voriteGIFs\x12\x42\n\x04gifs\x18\x01 \x03(\x0b\x32\x34.discord.FrecencyUserSettings.FavoriteGIFs.GifsEntry\x12\x14\n\x0chide_tooltip\x18\x02 \x01(\x08\x1a\xc3\x01\n\x0b\x46\x61voriteGIF\x12N\n\x06\x66ormat\x18\x01 \x01(\x0e\x32>.discord.FrecencyUserSettings.FavoriteGIFs.FavoriteGIF.GIFType\x12\x0b\n\x03src\x18\x02 \x01(\t\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r\x12\r\n\x05order\x18\x05 \x01(\r\")\n\x07GIFType\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\t\n\x05VIDEO\x10\x02\x1a\x63\n\tGifsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.discord.FrecencyUserSettings.FavoriteGIFs.FavoriteGIF:\x02\x38\x01\x1a\'\n\x10\x46\x61voriteStickers\x12\x13\n\x0bsticker_ids\x18\x01 \x03(\x10\x1a\xa8\x01\n\x0fStickerFrecency\x12M\n\x08stickers\x18\x01 \x03(\x0b\x32;.discord.FrecencyUserSettings.StickerFrecency.StickersEntry\x1a\x46\n\rStickersEntry\x12\x0b\n\x03key\x18\x01 \x01(\x10\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.discord.FrecencyItem:\x02\x38\x01\x1a \n\x0e\x46\x61voriteEmojis\x12\x0e\n\x06\x65mojis\x18\x01 \x03(\t\x1a\x9e\x01\n\rEmojiFrecency\x12G\n\x06\x65mojis\x18\x01 \x03(\x0b\x32\x37.discord.FrecencyUserSettings.EmojiFrecency.EmojisEntry\x1a\x44\n\x0b\x45mojisEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.discord.FrecencyItem:\x02\x38\x01\x1a\xe0\x01\n\x1a\x41pplicationCommandFrecency\x12o\n\x14\x61pplication_commands\x18\x01 \x03(\x0b\x32Q.discord.FrecencyUserSettings.ApplicationCommandFrecency.ApplicationCommandsEntry\x1aQ\n\x18\x41pplicationCommandsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.discord.FrecencyItem:\x02\x38\x01\x62\x06proto3')



_FRECENCYITEM = DESCRIPTOR.message_types_by_name['FrecencyItem']
_FRECENCYUSERSETTINGS = DESCRIPTOR.message_types_by_name['FrecencyUserSettings']
_FRECENCYUSERSETTINGS_VERSIONS = _FRECENCYUSERSETTINGS.nested_types_by_name['Versions']
_FRECENCYUSERSETTINGS_FAVORITEGIFS = _FRECENCYUSERSETTINGS.nested_types_by_name['FavoriteGIFs']
_FRECENCYUSERSETTINGS_FAVORITEGIFS_FAVORITEGIF = _FRECENCYUSERSETTINGS_FAVORITEGIFS.nested_types_by_name['FavoriteGIF']
_FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY = _FRECENCYUSERSETTINGS_FAVORITEGIFS.nested_types_by_name['GifsEntry']
_FRECENCYUSERSETTINGS_FAVORITESTICKERS = _FRECENCYUSERSETTINGS.nested_types_by_name['FavoriteStickers']
_FRECENCYUSERSETTINGS_STICKERFRECENCY = _FRECENCYUSERSETTINGS.nested_types_by_name['StickerFrecency']
_FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY = _FRECENCYUSERSETTINGS_STICKERFRECENCY.nested_types_by_name['StickersEntry']
_FRECENCYUSERSETTINGS_FAVORITEEMOJIS = _FRECENCYUSERSETTINGS.nested_types_by_name['FavoriteEmojis']
_FRECENCYUSERSETTINGS_EMOJIFRECENCY = _FRECENCYUSERSETTINGS.nested_types_by_name['EmojiFrecency']
_FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY = _FRECENCYUSERSETTINGS_EMOJIFRECENCY.nested_types_by_name['EmojisEntry']
_FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY = _FRECENCYUSERSETTINGS.nested_types_by_name['ApplicationCommandFrecency']
_FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY = _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY.nested_types_by_name['ApplicationCommandsEntry']
_FRECENCYUSERSETTINGS_FAVORITEGIFS_FAVORITEGIF_GIFTYPE = _FRECENCYUSERSETTINGS_FAVORITEGIFS_FAVORITEGIF.enum_types_by_name['GIFType']
FrecencyItem = _reflection.GeneratedProtocolMessageType('FrecencyItem', (_message.Message,), {
  'DESCRIPTOR' : _FRECENCYITEM,
  '__module__' : 'proto_pb2'
  # @@protoc_insertion_point(class_scope:discord.FrecencyItem)
  })
_sym_db.RegisterMessage(FrecencyItem)

FrecencyUserSettings = _reflection.GeneratedProtocolMessageType('FrecencyUserSettings', (_message.Message,), {

  'Versions' : _reflection.GeneratedProtocolMessageType('Versions', (_message.Message,), {
    'DESCRIPTOR' : _FRECENCYUSERSETTINGS_VERSIONS,
    '__module__' : 'proto_pb2'
    # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.Versions)
    })
  ,

  'FavoriteGIFs' : _reflection.GeneratedProtocolMessageType('FavoriteGIFs', (_message.Message,), {

    'FavoriteGIF' : _reflection.GeneratedProtocolMessageType('FavoriteGIF', (_message.Message,), {
      'DESCRIPTOR' : _FRECENCYUSERSETTINGS_FAVORITEGIFS_FAVORITEGIF,
      '__module__' : 'proto_pb2'
      # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.FavoriteGIFs.FavoriteGIF)
      })
    ,

    'GifsEntry' : _reflection.GeneratedProtocolMessageType('GifsEntry', (_message.Message,), {
      'DESCRIPTOR' : _FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY,
      '__module__' : 'proto_pb2'
      # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.FavoriteGIFs.GifsEntry)
      })
    ,
    'DESCRIPTOR' : _FRECENCYUSERSETTINGS_FAVORITEGIFS,
    '__module__' : 'proto_pb2'
    # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.FavoriteGIFs)
    })
  ,

  'FavoriteStickers' : _reflection.GeneratedProtocolMessageType('FavoriteStickers', (_message.Message,), {
    'DESCRIPTOR' : _FRECENCYUSERSETTINGS_FAVORITESTICKERS,
    '__module__' : 'proto_pb2'
    # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.FavoriteStickers)
    })
  ,

  'StickerFrecency' : _reflection.GeneratedProtocolMessageType('StickerFrecency', (_message.Message,), {

    'StickersEntry' : _reflection.GeneratedProtocolMessageType('StickersEntry', (_message.Message,), {
      'DESCRIPTOR' : _FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY,
      '__module__' : 'proto_pb2'
      # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.StickerFrecency.StickersEntry)
      })
    ,
    'DESCRIPTOR' : _FRECENCYUSERSETTINGS_STICKERFRECENCY,
    '__module__' : 'proto_pb2'
    # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.StickerFrecency)
    })
  ,

  'FavoriteEmojis' : _reflection.GeneratedProtocolMessageType('FavoriteEmojis', (_message.Message,), {
    'DESCRIPTOR' : _FRECENCYUSERSETTINGS_FAVORITEEMOJIS,
    '__module__' : 'proto_pb2'
    # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.FavoriteEmojis)
    })
  ,

  'EmojiFrecency' : _reflection.GeneratedProtocolMessageType('EmojiFrecency', (_message.Message,), {

    'EmojisEntry' : _reflection.GeneratedProtocolMessageType('EmojisEntry', (_message.Message,), {
      'DESCRIPTOR' : _FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY,
      '__module__' : 'proto_pb2'
      # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.EmojiFrecency.EmojisEntry)
      })
    ,
    'DESCRIPTOR' : _FRECENCYUSERSETTINGS_EMOJIFRECENCY,
    '__module__' : 'proto_pb2'
    # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.EmojiFrecency)
    })
  ,

  'ApplicationCommandFrecency' : _reflection.GeneratedProtocolMessageType('ApplicationCommandFrecency', (_message.Message,), {

    'ApplicationCommandsEntry' : _reflection.GeneratedProtocolMessageType('ApplicationCommandsEntry', (_message.Message,), {
      'DESCRIPTOR' : _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY,
      '__module__' : 'proto_pb2'
      # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.ApplicationCommandFrecency.ApplicationCommandsEntry)
      })
    ,
    'DESCRIPTOR' : _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY,
    '__module__' : 'proto_pb2'
    # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings.ApplicationCommandFrecency)
    })
  ,
  'DESCRIPTOR' : _FRECENCYUSERSETTINGS,
  '__module__' : 'proto_pb2'
  # @@protoc_insertion_point(class_scope:discord.FrecencyUserSettings)
  })
_sym_db.RegisterMessage(FrecencyUserSettings)
_sym_db.RegisterMessage(FrecencyUserSettings.Versions)
_sym_db.RegisterMessage(FrecencyUserSettings.FavoriteGIFs)
_sym_db.RegisterMessage(FrecencyUserSettings.FavoriteGIFs.FavoriteGIF)
_sym_db.RegisterMessage(FrecencyUserSettings.FavoriteGIFs.GifsEntry)
_sym_db.RegisterMessage(FrecencyUserSettings.FavoriteStickers)
_sym_db.RegisterMessage(FrecencyUserSettings.StickerFrecency)
_sym_db.RegisterMessage(FrecencyUserSettings.StickerFrecency.StickersEntry)
_sym_db.RegisterMessage(FrecencyUserSettings.FavoriteEmojis)
_sym_db.RegisterMessage(FrecencyUserSettings.EmojiFrecency)
_sym_db.RegisterMessage(FrecencyUserSettings.EmojiFrecency.EmojisEntry)
_sym_db.RegisterMessage(FrecencyUserSettings.ApplicationCommandFrecency)
_sym_db.RegisterMessage(FrecencyUserSettings.ApplicationCommandFrecency.ApplicationCommandsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY._options = None
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY._serialized_options = b'8\001'
  _FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY._options = None
  _FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY._serialized_options = b'8\001'
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY._options = None
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY._serialized_options = b'8\001'
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY._options = None
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY._serialized_options = b'8\001'
  _FRECENCYITEM._serialized_start=24
  _FRECENCYITEM._serialized_end=112
  _FRECENCYUSERSETTINGS._serialized_start=115
  _FRECENCYUSERSETTINGS._serialized_end=1768
  _FRECENCYUSERSETTINGS_VERSIONS._serialized_start=648
  _FRECENCYUSERSETTINGS_VERSIONS._serialized_end=728
  _FRECENCYUSERSETTINGS_FAVORITEGIFS._serialized_start=731
  _FRECENCYUSERSETTINGS_FAVORITEGIFS._serialized_end=1134
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_FAVORITEGIF._serialized_start=838
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_FAVORITEGIF._serialized_end=1033
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_FAVORITEGIF_GIFTYPE._serialized_start=992
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_FAVORITEGIF_GIFTYPE._serialized_end=1033
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY._serialized_start=1035
  _FRECENCYUSERSETTINGS_FAVORITEGIFS_GIFSENTRY._serialized_end=1134
  _FRECENCYUSERSETTINGS_FAVORITESTICKERS._serialized_start=1136
  _FRECENCYUSERSETTINGS_FAVORITESTICKERS._serialized_end=1175
  _FRECENCYUSERSETTINGS_STICKERFRECENCY._serialized_start=1178
  _FRECENCYUSERSETTINGS_STICKERFRECENCY._serialized_end=1346
  _FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY._serialized_start=1276
  _FRECENCYUSERSETTINGS_STICKERFRECENCY_STICKERSENTRY._serialized_end=1346
  _FRECENCYUSERSETTINGS_FAVORITEEMOJIS._serialized_start=1348
  _FRECENCYUSERSETTINGS_FAVORITEEMOJIS._serialized_end=1380
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY._serialized_start=1383
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY._serialized_end=1541
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY._serialized_start=1473
  _FRECENCYUSERSETTINGS_EMOJIFRECENCY_EMOJISENTRY._serialized_end=1541
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY._serialized_start=1544
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY._serialized_end=1768
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY._serialized_start=1687
  _FRECENCYUSERSETTINGS_APPLICATIONCOMMANDFRECENCY_APPLICATIONCOMMANDSENTRY._serialized_end=1768
# @@protoc_insertion_point(module_scope)
