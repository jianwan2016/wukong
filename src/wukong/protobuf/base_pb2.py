# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/base.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/base.proto',
  package='protobuf',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13protobuf/base.proto\x12\x08protobuf\"/\n\x04\x62\x61se\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x62\x06proto3'
)




_BASE = _descriptor.Descriptor(
  name='base',
  full_name='protobuf.base',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='protobuf.base.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protobuf.base.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=80,
)

DESCRIPTOR.message_types_by_name['base'] = _BASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

base = _reflection.GeneratedProtocolMessageType('base', (_message.Message,), {
  'DESCRIPTOR' : _BASE,
  '__module__' : 'protobuf.base_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.base)
  })
_sym_db.RegisterMessage(base)


# @@protoc_insertion_point(module_scope)
