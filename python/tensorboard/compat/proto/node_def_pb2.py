# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/compat/proto/node_def.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorboard.compat.proto import attr_value_pb2 as tensorboard_dot_compat_dot_proto_dot_attr__value__pb2
from tensorboard.compat.proto import full_type_pb2 as tensorboard_dot_compat_dot_proto_dot_full__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/compat/proto/node_def.proto',
  package='tensorboard',
  syntax='proto3',
  serialized_options=_b('\n\030org.tensorflow.frameworkB\tNodeProtoP\001ZOgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/node_def_go_proto\370\001\001'),
  serialized_pb=_b('\n\'tensorboard/compat/proto/node_def.proto\x12\x0btensorboard\x1a)tensorboard/compat/proto/attr_value.proto\x1a(tensorboard/compat/proto/full_type.proto\"\x8a\x03\n\x07NodeDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02op\x18\x02 \x01(\t\x12\r\n\x05input\x18\x03 \x03(\t\x12\x0e\n\x06\x64\x65vice\x18\x04 \x01(\t\x12,\n\x04\x61ttr\x18\x05 \x03(\x0b\x32\x1e.tensorboard.NodeDef.AttrEntry\x12K\n\x17\x65xperimental_debug_info\x18\x06 \x01(\x0b\x32*.tensorboard.NodeDef.ExperimentalDebugInfo\x12\x33\n\x11\x65xperimental_type\x18\x07 \x01(\x0b\x32\x18.tensorboard.FullTypeDef\x1a\x43\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.tensorboard.AttrValue:\x02\x38\x01\x1aQ\n\x15\x45xperimentalDebugInfo\x12\x1b\n\x13original_node_names\x18\x01 \x03(\t\x12\x1b\n\x13original_func_names\x18\x02 \x03(\tB{\n\x18org.tensorflow.frameworkB\tNodeProtoP\x01ZOgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/node_def_go_proto\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorboard_dot_compat_dot_proto_dot_attr__value__pb2.DESCRIPTOR,tensorboard_dot_compat_dot_proto_dot_full__type__pb2.DESCRIPTOR,])




_NODEDEF_ATTRENTRY = _descriptor.Descriptor(
  name='AttrEntry',
  full_name='tensorboard.NodeDef.AttrEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorboard.NodeDef.AttrEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorboard.NodeDef.AttrEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=453,
)

_NODEDEF_EXPERIMENTALDEBUGINFO = _descriptor.Descriptor(
  name='ExperimentalDebugInfo',
  full_name='tensorboard.NodeDef.ExperimentalDebugInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='original_node_names', full_name='tensorboard.NodeDef.ExperimentalDebugInfo.original_node_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original_func_names', full_name='tensorboard.NodeDef.ExperimentalDebugInfo.original_func_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=455,
  serialized_end=536,
)

_NODEDEF = _descriptor.Descriptor(
  name='NodeDef',
  full_name='tensorboard.NodeDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorboard.NodeDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='tensorboard.NodeDef.op', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input', full_name='tensorboard.NodeDef.input', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='tensorboard.NodeDef.device', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attr', full_name='tensorboard.NodeDef.attr', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experimental_debug_info', full_name='tensorboard.NodeDef.experimental_debug_info', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experimental_type', full_name='tensorboard.NodeDef.experimental_type', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NODEDEF_ATTRENTRY, _NODEDEF_EXPERIMENTALDEBUGINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=536,
)

_NODEDEF_ATTRENTRY.fields_by_name['value'].message_type = tensorboard_dot_compat_dot_proto_dot_attr__value__pb2._ATTRVALUE
_NODEDEF_ATTRENTRY.containing_type = _NODEDEF
_NODEDEF_EXPERIMENTALDEBUGINFO.containing_type = _NODEDEF
_NODEDEF.fields_by_name['attr'].message_type = _NODEDEF_ATTRENTRY
_NODEDEF.fields_by_name['experimental_debug_info'].message_type = _NODEDEF_EXPERIMENTALDEBUGINFO
_NODEDEF.fields_by_name['experimental_type'].message_type = tensorboard_dot_compat_dot_proto_dot_full__type__pb2._FULLTYPEDEF
DESCRIPTOR.message_types_by_name['NodeDef'] = _NODEDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeDef = _reflection.GeneratedProtocolMessageType('NodeDef', (_message.Message,), {

  'AttrEntry' : _reflection.GeneratedProtocolMessageType('AttrEntry', (_message.Message,), {
    'DESCRIPTOR' : _NODEDEF_ATTRENTRY,
    '__module__' : 'tensorboard.compat.proto.node_def_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.NodeDef.AttrEntry)
    })
  ,

  'ExperimentalDebugInfo' : _reflection.GeneratedProtocolMessageType('ExperimentalDebugInfo', (_message.Message,), {
    'DESCRIPTOR' : _NODEDEF_EXPERIMENTALDEBUGINFO,
    '__module__' : 'tensorboard.compat.proto.node_def_pb2'
    # @@protoc_insertion_point(class_scope:tensorboard.NodeDef.ExperimentalDebugInfo)
    })
  ,
  'DESCRIPTOR' : _NODEDEF,
  '__module__' : 'tensorboard.compat.proto.node_def_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.NodeDef)
  })
_sym_db.RegisterMessage(NodeDef)
_sym_db.RegisterMessage(NodeDef.AttrEntry)
_sym_db.RegisterMessage(NodeDef.ExperimentalDebugInfo)


DESCRIPTOR._options = None
_NODEDEF_ATTRENTRY._options = None
# @@protoc_insertion_point(module_scope)