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
  serialized_pb=_b('\n\x1brequests_mercadolibre.proto\x12\x03\x61pi\"\x1f\n\x0bPingMessage\x12\x10\n\x08greeting\x18\x01 \x01(\t28\n\x04Ping\x12\x30\n\x08SayHello\x12\x10.api.PingMessage\x1a\x10.api.PingMessage\"\x00\x62\x06proto3')
)




_PINGMESSAGE = _descriptor.Descriptor(
  name='PingMessage',
  full_name='api.PingMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='api.PingMessage.greeting', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_end=67,
)

DESCRIPTOR.message_types_by_name['PingMessage'] = _PINGMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingMessage = _reflection.GeneratedProtocolMessageType('PingMessage', (_message.Message,), dict(
  DESCRIPTOR = _PINGMESSAGE,
  __module__ = 'requests_mercadolibre_pb2'
  # @@protoc_insertion_point(class_scope:api.PingMessage)
  ))
_sym_db.RegisterMessage(PingMessage)



_PING = _descriptor.ServiceDescriptor(
  name='Ping',
  full_name='api.Ping',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=69,
  serialized_end=125,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='api.Ping.SayHello',
    index=0,
    containing_service=None,
    input_type=_PINGMESSAGE,
    output_type=_PINGMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PING)

DESCRIPTOR.services_by_name['Ping'] = _PING

# @@protoc_insertion_point(module_scope)
