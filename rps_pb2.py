# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rps.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\trps.proto\x12\x13rock_paper_scissors\"\"\n\x0bGameRequest\x12\x13\n\x0bplayer_move\x18\x01 \x01(\x05\"/\n\x0cGameResponse\x12\x0f\n\x07\x61i_move\x18\x01 \x01(\x05\x12\x0e\n\x06winner\x18\x02 \x01(\x05\x32\x66\n\x11RockPaperScissors\x12Q\n\x08PlayGame\x12 .rock_paper_scissors.GameRequest\x1a!.rock_paper_scissors.GameResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rps_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GAMEREQUEST']._serialized_start=34
  _globals['_GAMEREQUEST']._serialized_end=68
  _globals['_GAMERESPONSE']._serialized_start=70
  _globals['_GAMERESPONSE']._serialized_end=117
  _globals['_ROCKPAPERSCISSORS']._serialized_start=119
  _globals['_ROCKPAPERSCISSORS']._serialized_end=221
# @@protoc_insertion_point(module_scope)