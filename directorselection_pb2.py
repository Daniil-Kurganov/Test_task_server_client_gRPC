# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: directorselection.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x64irectorselection.proto\x12\x11\x64irectorselection\"(\n\x07Request\x12\x1d\n\x15string_directory_path\x18\x01 \x01(\t\"\x18\n\x05Reply\x12\x0f\n\x07message\x18\x01 \x01(\t2g\n\x1cGetInformationAboutDirectory\x12G\n\rDirectoryCall\x12\x1a.directorselection.Request\x1a\x18.directorselection.Reply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'directorselection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=46
  _globals['_REQUEST']._serialized_end=86
  _globals['_REPLY']._serialized_start=88
  _globals['_REPLY']._serialized_end=112
  _globals['_GETINFORMATIONABOUTDIRECTORY']._serialized_start=114
  _globals['_GETINFORMATIONABOUTDIRECTORY']._serialized_end=217
# @@protoc_insertion_point(module_scope)
