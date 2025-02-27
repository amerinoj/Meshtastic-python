# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: portnums.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='portnums.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\023com.geeksville.meshB\010PortnumsH\003Z!github.com/meshtastic/gomeshproto',
  serialized_pb=b'\n\x0eportnums.proto*\xbb\x02\n\x07PortNum\x12\x0f\n\x0bUNKNOWN_APP\x10\x00\x12\x14\n\x10TEXT_MESSAGE_APP\x10\x01\x12\x17\n\x13REMOTE_HARDWARE_APP\x10\x02\x12\x10\n\x0cPOSITION_APP\x10\x03\x12\x10\n\x0cNODEINFO_APP\x10\x04\x12\x0f\n\x0bROUTING_APP\x10\x05\x12\r\n\tADMIN_APP\x10\x06\x12\r\n\tREPLY_APP\x10 \x12\x11\n\rIP_TUNNEL_APP\x10!\x12\x0e\n\nSERIAL_APP\x10@\x12\x15\n\x11STORE_FORWARD_APP\x10\x41\x12\x12\n\x0eRANGE_TEST_APP\x10\x42\x12\x11\n\rTELEMETRY_APP\x10\x43\x12\x0b\n\x07ZPS_APP\x10\x44\x12\x10\n\x0bPRIVATE_APP\x10\x80\x02\x12\x13\n\x0e\x41TAK_FORWARDER\x10\x81\x02\x12\x08\n\x03MAX\x10\xff\x03\x42\x44\n\x13\x63om.geeksville.meshB\x08PortnumsH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3'
)

_PORTNUM = _descriptor.EnumDescriptor(
  name='PortNum',
  full_name='PortNum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_APP', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_MESSAGE_APP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_HARDWARE_APP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSITION_APP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NODEINFO_APP', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROUTING_APP', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADMIN_APP', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLY_APP', index=7, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IP_TUNNEL_APP', index=8, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERIAL_APP', index=9, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORE_FORWARD_APP', index=10, number=65,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANGE_TEST_APP', index=11, number=66,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TELEMETRY_APP', index=12, number=67,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZPS_APP', index=13, number=68,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIVATE_APP', index=14, number=256,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATAK_FORWARDER', index=15, number=257,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX', index=16, number=511,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=19,
  serialized_end=334,
)
_sym_db.RegisterEnumDescriptor(_PORTNUM)

PortNum = enum_type_wrapper.EnumTypeWrapper(_PORTNUM)
UNKNOWN_APP = 0
TEXT_MESSAGE_APP = 1
REMOTE_HARDWARE_APP = 2
POSITION_APP = 3
NODEINFO_APP = 4
ROUTING_APP = 5
ADMIN_APP = 6
REPLY_APP = 32
IP_TUNNEL_APP = 33
SERIAL_APP = 64
STORE_FORWARD_APP = 65
RANGE_TEST_APP = 66
TELEMETRY_APP = 67
ZPS_APP = 68
PRIVATE_APP = 256
ATAK_FORWARDER = 257
MAX = 511


DESCRIPTOR.enum_types_by_name['PortNum'] = _PORTNUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
