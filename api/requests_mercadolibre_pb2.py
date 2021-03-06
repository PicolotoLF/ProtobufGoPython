# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: requests_mercadolibre.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='requests_mercadolibre.proto',
  package='api',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1brequests_mercadolibre.proto\x12\x03\x61pi\"\x18\n\x08ListURLs\x12\x0c\n\x04urls\x18\x01 \x03(\t\"\x14\n\x04Resp\x12\x0c\n\x04resp\x18\x01 \x03(\t22\n\x07Request\x12\'\n\tRequestGo\x12\r.api.ListURLs\x1a\t.api.Resp\"\x00\x62\x06proto3')
)




_LISTURLS = _descriptor.Descriptor(
  name='ListURLs',
  full_name='api.ListURLs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='urls', full_name='api.ListURLs.urls', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=36,
  serialized_end=60,
)


_RESP = _descriptor.Descriptor(
  name='Resp',
  full_name='api.Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='api.Resp.resp', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=62,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['ListURLs'] = _LISTURLS
DESCRIPTOR.message_types_by_name['Resp'] = _RESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListURLs = _reflection.GeneratedProtocolMessageType('ListURLs', (_message.Message,), dict(
  DESCRIPTOR = _LISTURLS,
  __module__ = 'requests_mercadolibre_pb2'
  # @@protoc_insertion_point(class_scope:api.ListURLs)
  ))
_sym_db.RegisterMessage(ListURLs)

Resp = _reflection.GeneratedProtocolMessageType('Resp', (_message.Message,), dict(
  DESCRIPTOR = _RESP,
  __module__ = 'requests_mercadolibre_pb2'
  # @@protoc_insertion_point(class_scope:api.Resp)
  ))
_sym_db.RegisterMessage(Resp)



_REQUEST = _descriptor.ServiceDescriptor(
  name='Request',
  full_name='api.Request',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=84,
  serialized_end=134,
  methods=[
  _descriptor.MethodDescriptor(
    name='RequestGo',
    full_name='api.Request.RequestGo',
    index=0,
    containing_service=None,
    input_type=_LISTURLS,
    output_type=_RESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_REQUEST)

DESCRIPTOR.services_by_name['Request'] = _REQUEST

# @@protoc_insertion_point(module_scope)
