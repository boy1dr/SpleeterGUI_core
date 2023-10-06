# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/compat/proto/event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorboard.compat.proto import summary_pb2 as tensorboard_dot_compat_dot_proto_dot_summary__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/compat/proto/event.proto',
  package='tensorboard',
  syntax='proto3',
  serialized_options=_b('\n\023org.tensorflow.utilB\013EventProtosP\001ZGgithub.com/tensorflow/tensorflow/tensorflow/go/core/util/event_go_proto\370\001\001'),
  serialized_pb=_b('\n$tensorboard/compat/proto/event.proto\x12\x0btensorboard\x1a&tensorboard/compat/proto/summary.proto\"\xc3\x02\n\x05\x45vent\x12\x11\n\twall_time\x18\x01 \x01(\x01\x12\x0c\n\x04step\x18\x02 \x01(\x03\x12\x16\n\x0c\x66ile_version\x18\x03 \x01(\tH\x00\x12\x13\n\tgraph_def\x18\x04 \x01(\x0cH\x00\x12\'\n\x07summary\x18\x05 \x01(\x0b\x32\x14.tensorboard.SummaryH\x00\x12\x32\n\x0blog_message\x18\x06 \x01(\x0b\x32\x17.tensorboard.LogMessageB\x02\x18\x01H\x00\x12.\n\x0bsession_log\x18\x07 \x01(\x0b\x32\x17.tensorboard.SessionLogH\x00\x12=\n\x13tagged_run_metadata\x18\x08 \x01(\x0b\x32\x1e.tensorboard.TaggedRunMetadataH\x00\x12\x18\n\x0emeta_graph_def\x18\t \x01(\x0cH\x00\x42\x06\n\x04what\"\xa2\x01\n\nLogMessage\x12,\n\x05level\x18\x01 \x01(\x0e\x32\x1d.tensorboard.LogMessage.Level\x12\x0f\n\x07message\x18\x02 \x01(\t\"Q\n\x05Level\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tDEBUGGING\x10\n\x12\x08\n\x04INFO\x10\x14\x12\x08\n\x04WARN\x10\x1e\x12\t\n\x05\x45RROR\x10(\x12\t\n\x05\x46\x41TAL\x10\x32\x1a\x02\x18\x01:\x02\x18\x01\"\xb7\x01\n\nSessionLog\x12\x35\n\x06status\x18\x01 \x01(\x0e\x32%.tensorboard.SessionLog.SessionStatus\x12\x17\n\x0f\x63heckpoint_path\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\"L\n\rSessionStatus\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\t\n\x05START\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\x0e\n\nCHECKPOINT\x10\x03\"6\n\x11TaggedRunMetadata\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x14\n\x0crun_metadata\x18\x02 \x01(\x0c\"$\n\x0eWatchdogConfig\x12\x12\n\ntimeout_ms\x18\x01 \x01(\x03\"&\n\x11RequestedExitCode\x12\x11\n\texit_code\x18\x01 \x01(\x05\"\xb9\x01\n\x16WorkerHeartbeatRequest\x12\x36\n\rshutdown_mode\x18\x01 \x01(\x0e\x32\x1f.tensorboard.WorkerShutdownMode\x12\x34\n\x0fwatchdog_config\x18\x02 \x01(\x0b\x32\x1b.tensorboard.WatchdogConfig\x12\x31\n\texit_code\x18\x03 \x01(\x0b\x32\x1e.tensorboard.RequestedExitCode\"\x85\x01\n\x17WorkerHeartbeatResponse\x12\x30\n\rhealth_status\x18\x01 \x01(\x0e\x32\x19.tensorboard.WorkerHealth\x12&\n\nworker_log\x18\x02 \x03(\x0b\x32\x12.tensorboard.Event\x12\x10\n\x08hostname\x18\x03 \x01(\t*[\n\x0cWorkerHealth\x12\x06\n\x02OK\x10\x00\x12\x1c\n\x18RECEIVED_SHUTDOWN_SIGNAL\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x11\n\rSHUTTING_DOWN\x10\x03*k\n\x12WorkerShutdownMode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x12\n\x0eNOT_CONFIGURED\x10\x01\x12\x18\n\x14WAIT_FOR_COORDINATOR\x10\x02\x12\x1a\n\x16SHUTDOWN_AFTER_TIMEOUT\x10\x03\x42p\n\x13org.tensorflow.utilB\x0b\x45ventProtosP\x01ZGgithub.com/tensorflow/tensorflow/tensorflow/go/core/util/event_go_proto\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorboard_dot_compat_dot_proto_dot_summary__pb2.DESCRIPTOR,])

_WORKERHEALTH = _descriptor.EnumDescriptor(
  name='WorkerHealth',
  full_name='tensorboard.WorkerHealth',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECEIVED_SHUTDOWN_SIGNAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUTTING_DOWN', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1228,
  serialized_end=1319,
)
_sym_db.RegisterEnumDescriptor(_WORKERHEALTH)

WorkerHealth = enum_type_wrapper.EnumTypeWrapper(_WORKERHEALTH)
_WORKERSHUTDOWNMODE = _descriptor.EnumDescriptor(
  name='WorkerShutdownMode',
  full_name='tensorboard.WorkerShutdownMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_CONFIGURED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAIT_FOR_COORDINATOR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN_AFTER_TIMEOUT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1321,
  serialized_end=1428,
)
_sym_db.RegisterEnumDescriptor(_WORKERSHUTDOWNMODE)

WorkerShutdownMode = enum_type_wrapper.EnumTypeWrapper(_WORKERSHUTDOWNMODE)
OK = 0
RECEIVED_SHUTDOWN_SIGNAL = 1
INTERNAL_ERROR = 2
SHUTTING_DOWN = 3
DEFAULT = 0
NOT_CONFIGURED = 1
WAIT_FOR_COORDINATOR = 2
SHUTDOWN_AFTER_TIMEOUT = 3


_LOGMESSAGE_LEVEL = _descriptor.EnumDescriptor(
  name='Level',
  full_name='tensorboard.LogMessage.Level',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBUGGING', index=1, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFO', index=2, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARN', index=3, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=4, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FATAL', index=5, number=50,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=_b('\030\001'),
  serialized_start=497,
  serialized_end=578,
)
_sym_db.RegisterEnumDescriptor(_LOGMESSAGE_LEVEL)

_SESSIONLOG_SESSIONSTATUS = _descriptor.EnumDescriptor(
  name='SessionStatus',
  full_name='tensorboard.SessionLog.SessionStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECKPOINT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=692,
  serialized_end=768,
)
_sym_db.RegisterEnumDescriptor(_SESSIONLOG_SESSIONSTATUS)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='tensorboard.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wall_time', full_name='tensorboard.Event.wall_time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='tensorboard.Event.step', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_version', full_name='tensorboard.Event.file_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graph_def', full_name='tensorboard.Event.graph_def', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='summary', full_name='tensorboard.Event.summary', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_message', full_name='tensorboard.Event.log_message', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_log', full_name='tensorboard.Event.session_log', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagged_run_metadata', full_name='tensorboard.Event.tagged_run_metadata', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta_graph_def', full_name='tensorboard.Event.meta_graph_def', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
    _descriptor.OneofDescriptor(
      name='what', full_name='tensorboard.Event.what',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=94,
  serialized_end=417,
)


_LOGMESSAGE = _descriptor.Descriptor(
  name='LogMessage',
  full_name='tensorboard.LogMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='tensorboard.LogMessage.level', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='tensorboard.LogMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOGMESSAGE_LEVEL,
  ],
  serialized_options=_b('\030\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=582,
)


_SESSIONLOG = _descriptor.Descriptor(
  name='SessionLog',
  full_name='tensorboard.SessionLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='tensorboard.SessionLog.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_path', full_name='tensorboard.SessionLog.checkpoint_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='tensorboard.SessionLog.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SESSIONLOG_SESSIONSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=768,
)


_TAGGEDRUNMETADATA = _descriptor.Descriptor(
  name='TaggedRunMetadata',
  full_name='tensorboard.TaggedRunMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='tensorboard.TaggedRunMetadata.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_metadata', full_name='tensorboard.TaggedRunMetadata.run_metadata', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=770,
  serialized_end=824,
)


_WATCHDOGCONFIG = _descriptor.Descriptor(
  name='WatchdogConfig',
  full_name='tensorboard.WatchdogConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout_ms', full_name='tensorboard.WatchdogConfig.timeout_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=826,
  serialized_end=862,
)


_REQUESTEDEXITCODE = _descriptor.Descriptor(
  name='RequestedExitCode',
  full_name='tensorboard.RequestedExitCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exit_code', full_name='tensorboard.RequestedExitCode.exit_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=864,
  serialized_end=902,
)


_WORKERHEARTBEATREQUEST = _descriptor.Descriptor(
  name='WorkerHeartbeatRequest',
  full_name='tensorboard.WorkerHeartbeatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shutdown_mode', full_name='tensorboard.WorkerHeartbeatRequest.shutdown_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='watchdog_config', full_name='tensorboard.WorkerHeartbeatRequest.watchdog_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_code', full_name='tensorboard.WorkerHeartbeatRequest.exit_code', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=905,
  serialized_end=1090,
)


_WORKERHEARTBEATRESPONSE = _descriptor.Descriptor(
  name='WorkerHeartbeatResponse',
  full_name='tensorboard.WorkerHeartbeatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='health_status', full_name='tensorboard.WorkerHeartbeatResponse.health_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='worker_log', full_name='tensorboard.WorkerHeartbeatResponse.worker_log', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='tensorboard.WorkerHeartbeatResponse.hostname', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1093,
  serialized_end=1226,
)

_EVENT.fields_by_name['summary'].message_type = tensorboard_dot_compat_dot_proto_dot_summary__pb2._SUMMARY
_EVENT.fields_by_name['log_message'].message_type = _LOGMESSAGE
_EVENT.fields_by_name['session_log'].message_type = _SESSIONLOG
_EVENT.fields_by_name['tagged_run_metadata'].message_type = _TAGGEDRUNMETADATA
_EVENT.oneofs_by_name['what'].fields.append(
  _EVENT.fields_by_name['file_version'])
_EVENT.fields_by_name['file_version'].containing_oneof = _EVENT.oneofs_by_name['what']
_EVENT.oneofs_by_name['what'].fields.append(
  _EVENT.fields_by_name['graph_def'])
_EVENT.fields_by_name['graph_def'].containing_oneof = _EVENT.oneofs_by_name['what']
_EVENT.oneofs_by_name['what'].fields.append(
  _EVENT.fields_by_name['summary'])
_EVENT.fields_by_name['summary'].containing_oneof = _EVENT.oneofs_by_name['what']
_EVENT.oneofs_by_name['what'].fields.append(
  _EVENT.fields_by_name['log_message'])
_EVENT.fields_by_name['log_message'].containing_oneof = _EVENT.oneofs_by_name['what']
_EVENT.oneofs_by_name['what'].fields.append(
  _EVENT.fields_by_name['session_log'])
_EVENT.fields_by_name['session_log'].containing_oneof = _EVENT.oneofs_by_name['what']
_EVENT.oneofs_by_name['what'].fields.append(
  _EVENT.fields_by_name['tagged_run_metadata'])
_EVENT.fields_by_name['tagged_run_metadata'].containing_oneof = _EVENT.oneofs_by_name['what']
_EVENT.oneofs_by_name['what'].fields.append(
  _EVENT.fields_by_name['meta_graph_def'])
_EVENT.fields_by_name['meta_graph_def'].containing_oneof = _EVENT.oneofs_by_name['what']
_LOGMESSAGE.fields_by_name['level'].enum_type = _LOGMESSAGE_LEVEL
_LOGMESSAGE_LEVEL.containing_type = _LOGMESSAGE
_SESSIONLOG.fields_by_name['status'].enum_type = _SESSIONLOG_SESSIONSTATUS
_SESSIONLOG_SESSIONSTATUS.containing_type = _SESSIONLOG
_WORKERHEARTBEATREQUEST.fields_by_name['shutdown_mode'].enum_type = _WORKERSHUTDOWNMODE
_WORKERHEARTBEATREQUEST.fields_by_name['watchdog_config'].message_type = _WATCHDOGCONFIG
_WORKERHEARTBEATREQUEST.fields_by_name['exit_code'].message_type = _REQUESTEDEXITCODE
_WORKERHEARTBEATRESPONSE.fields_by_name['health_status'].enum_type = _WORKERHEALTH
_WORKERHEARTBEATRESPONSE.fields_by_name['worker_log'].message_type = _EVENT
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['LogMessage'] = _LOGMESSAGE
DESCRIPTOR.message_types_by_name['SessionLog'] = _SESSIONLOG
DESCRIPTOR.message_types_by_name['TaggedRunMetadata'] = _TAGGEDRUNMETADATA
DESCRIPTOR.message_types_by_name['WatchdogConfig'] = _WATCHDOGCONFIG
DESCRIPTOR.message_types_by_name['RequestedExitCode'] = _REQUESTEDEXITCODE
DESCRIPTOR.message_types_by_name['WorkerHeartbeatRequest'] = _WORKERHEARTBEATREQUEST
DESCRIPTOR.message_types_by_name['WorkerHeartbeatResponse'] = _WORKERHEARTBEATRESPONSE
DESCRIPTOR.enum_types_by_name['WorkerHealth'] = _WORKERHEALTH
DESCRIPTOR.enum_types_by_name['WorkerShutdownMode'] = _WORKERSHUTDOWNMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'tensorboard.compat.proto.event_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.Event)
  })
_sym_db.RegisterMessage(Event)

LogMessage = _reflection.GeneratedProtocolMessageType('LogMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOGMESSAGE,
  '__module__' : 'tensorboard.compat.proto.event_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.LogMessage)
  })
_sym_db.RegisterMessage(LogMessage)

SessionLog = _reflection.GeneratedProtocolMessageType('SessionLog', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONLOG,
  '__module__' : 'tensorboard.compat.proto.event_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.SessionLog)
  })
_sym_db.RegisterMessage(SessionLog)

TaggedRunMetadata = _reflection.GeneratedProtocolMessageType('TaggedRunMetadata', (_message.Message,), {
  'DESCRIPTOR' : _TAGGEDRUNMETADATA,
  '__module__' : 'tensorboard.compat.proto.event_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.TaggedRunMetadata)
  })
_sym_db.RegisterMessage(TaggedRunMetadata)

WatchdogConfig = _reflection.GeneratedProtocolMessageType('WatchdogConfig', (_message.Message,), {
  'DESCRIPTOR' : _WATCHDOGCONFIG,
  '__module__' : 'tensorboard.compat.proto.event_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.WatchdogConfig)
  })
_sym_db.RegisterMessage(WatchdogConfig)

RequestedExitCode = _reflection.GeneratedProtocolMessageType('RequestedExitCode', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTEDEXITCODE,
  '__module__' : 'tensorboard.compat.proto.event_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.RequestedExitCode)
  })
_sym_db.RegisterMessage(RequestedExitCode)

WorkerHeartbeatRequest = _reflection.GeneratedProtocolMessageType('WorkerHeartbeatRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKERHEARTBEATREQUEST,
  '__module__' : 'tensorboard.compat.proto.event_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.WorkerHeartbeatRequest)
  })
_sym_db.RegisterMessage(WorkerHeartbeatRequest)

WorkerHeartbeatResponse = _reflection.GeneratedProtocolMessageType('WorkerHeartbeatResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKERHEARTBEATRESPONSE,
  '__module__' : 'tensorboard.compat.proto.event_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.WorkerHeartbeatResponse)
  })
_sym_db.RegisterMessage(WorkerHeartbeatResponse)


DESCRIPTOR._options = None
_EVENT.fields_by_name['log_message']._options = None
_LOGMESSAGE_LEVEL._options = None
_LOGMESSAGE._options = None
# @@protoc_insertion_point(module_scope)
