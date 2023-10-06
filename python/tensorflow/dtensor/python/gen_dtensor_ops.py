"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
"""

import collections

from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import context as _context
from tensorflow.python.eager import core as _core
from tensorflow.python.eager import execute as _execute
from tensorflow.python.framework import dtypes as _dtypes

from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library
from tensorflow.python.util.deprecation import deprecated_endpoints
from tensorflow.python.util import dispatch as _dispatch
from tensorflow.python.util.tf_export import tf_export

from typing import TypeVar

@_dispatch.add_fallback_dispatch_list
@_dispatch.add_type_based_api_dispatcher
@tf_export('configure_and_initialize_global_tpu')
def configure_and_initialize_global_tpu(name=None):
  r"""An op that sets up the centralized structures for a distributed TPU

  system.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
    A vector containing the global TPU id of each TPU on the host.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "ConfigureAndInitializeGlobalTPU", name)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      _result = _dispatcher_for_configure_and_initialize_global_tpu(
          (name,), None)
      if _result is not NotImplemented:
        return _result
      return configure_and_initialize_global_tpu_eager_fallback(
          name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      _result = _dispatch.dispatch(
            configure_and_initialize_global_tpu, (), dict(name=name)
          )
      if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return _result
      raise
  else:
    _result = _dispatcher_for_configure_and_initialize_global_tpu(
        (name,), None)
    if _result is not NotImplemented:
      return _result
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "ConfigureAndInitializeGlobalTPU", name=name)
  except (TypeError, ValueError):
    _result = _dispatch.dispatch(
          configure_and_initialize_global_tpu, (), dict(name=name)
        )
    if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return _result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ()
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "ConfigureAndInitializeGlobalTPU", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

ConfigureAndInitializeGlobalTPU = tf_export("raw_ops.ConfigureAndInitializeGlobalTPU")(_ops.to_raw_op(configure_and_initialize_global_tpu))
_dispatcher_for_configure_and_initialize_global_tpu = configure_and_initialize_global_tpu._tf_type_based_dispatcher.Dispatch


def configure_and_initialize_global_tpu_eager_fallback(name, ctx):
  _inputs_flat = []
  _attrs = None
  _result = _execute.execute(b"ConfigureAndInitializeGlobalTPU", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=ctx,
                             name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "ConfigureAndInitializeGlobalTPU", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_fallback_dispatch_list
@_dispatch.add_type_based_api_dispatcher
@tf_export('copy_to_mesh')
def copy_to_mesh(input, layout, source_layout="", name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor`.
    layout: A `string`.
    source_layout: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "CopyToMesh", name, input, "layout", layout, "source_layout",
        source_layout)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      _result = _dispatcher_for_copy_to_mesh(
          (input, layout, source_layout, name,), None)
      if _result is not NotImplemented:
        return _result
      return copy_to_mesh_eager_fallback(
          input, layout=layout, source_layout=source_layout, name=name,
          ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      _result = _dispatch.dispatch(
            copy_to_mesh, (), dict(input=input, layout=layout,
                                   source_layout=source_layout, name=name)
          )
      if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return _result
      raise
  else:
    _result = _dispatcher_for_copy_to_mesh(
        (input, layout, source_layout, name,), None)
    if _result is not NotImplemented:
      return _result
  # Add nodes to the TensorFlow graph.
  layout = _execute.make_str(layout, "layout")
  if source_layout is None:
    source_layout = ""
  source_layout = _execute.make_str(source_layout, "source_layout")
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "CopyToMesh", input=input, layout=layout, source_layout=source_layout,
                      name=name)
  except (TypeError, ValueError):
    _result = _dispatch.dispatch(
          copy_to_mesh, (), dict(input=input, layout=layout,
                                 source_layout=source_layout, name=name)
        )
    if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return _result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("layout", _op.get_attr("layout"), "source_layout",
              _op.get_attr("source_layout"), "T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "CopyToMesh", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

CopyToMesh = tf_export("raw_ops.CopyToMesh")(_ops.to_raw_op(copy_to_mesh))
_dispatcher_for_copy_to_mesh = copy_to_mesh._tf_type_based_dispatcher.Dispatch


def copy_to_mesh_eager_fallback(input, layout, source_layout, name, ctx):
  layout = _execute.make_str(layout, "layout")
  if source_layout is None:
    source_layout = ""
  source_layout = _execute.make_str(source_layout, "source_layout")
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx, [])
  _inputs_flat = [input]
  _attrs = ("layout", layout, "source_layout", source_layout, "T", _attr_T)
  _result = _execute.execute(b"CopyToMesh", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "CopyToMesh", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_fallback_dispatch_list
@_dispatch.add_type_based_api_dispatcher
@tf_export('d_tensor_restore_v2')
def d_tensor_restore_v2(prefix, tensor_names, shape_and_slices, input_shapes, input_layouts, dtypes, name=None):
  r"""TODO: add doc.

  Args:
    prefix: A `Tensor` of type `string`.
    tensor_names: A `Tensor` of type `string`.
    shape_and_slices: A `Tensor` of type `string`.
    input_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`).
    input_layouts: A list of `strings`.
    dtypes: A list of `tf.DTypes` that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `dtypes`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "DTensorRestoreV2", name, prefix, tensor_names,
        shape_and_slices, "input_shapes", input_shapes, "input_layouts",
        input_layouts, "dtypes", dtypes)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      _result = _dispatcher_for_d_tensor_restore_v2(
          (prefix, tensor_names, shape_and_slices, input_shapes,
          input_layouts, dtypes, name,), None)
      if _result is not NotImplemented:
        return _result
      return d_tensor_restore_v2_eager_fallback(
          prefix, tensor_names, shape_and_slices, input_shapes=input_shapes,
          input_layouts=input_layouts, dtypes=dtypes, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      _result = _dispatch.dispatch(
            d_tensor_restore_v2, (), dict(prefix=prefix,
                                          tensor_names=tensor_names,
                                          shape_and_slices=shape_and_slices,
                                          input_shapes=input_shapes,
                                          input_layouts=input_layouts,
                                          dtypes=dtypes, name=name)
          )
      if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return _result
      raise
  else:
    _result = _dispatcher_for_d_tensor_restore_v2(
        (prefix, tensor_names, shape_and_slices, input_shapes, input_layouts,
        dtypes, name,), None)
    if _result is not NotImplemented:
      return _result
  # Add nodes to the TensorFlow graph.
  if not isinstance(input_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'input_shapes' argument to "
        "'d_tensor_restore_v2' Op, not %r." % input_shapes)
  input_shapes = [_execute.make_shape(_s, "input_shapes") for _s in input_shapes]
  if not isinstance(input_layouts, (list, tuple)):
    raise TypeError(
        "Expected list for 'input_layouts' argument to "
        "'d_tensor_restore_v2' Op, not %r." % input_layouts)
  input_layouts = [_execute.make_str(_s, "input_layouts") for _s in input_layouts]
  if not isinstance(dtypes, (list, tuple)):
    raise TypeError(
        "Expected list for 'dtypes' argument to "
        "'d_tensor_restore_v2' Op, not %r." % dtypes)
  dtypes = [_execute.make_type(_t, "dtypes") for _t in dtypes]
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "DTensorRestoreV2", prefix=prefix, tensor_names=tensor_names,
                            shape_and_slices=shape_and_slices,
                            input_shapes=input_shapes,
                            input_layouts=input_layouts, dtypes=dtypes,
                            name=name)
  except (TypeError, ValueError):
    _result = _dispatch.dispatch(
          d_tensor_restore_v2, (), dict(prefix=prefix,
                                        tensor_names=tensor_names,
                                        shape_and_slices=shape_and_slices,
                                        input_shapes=input_shapes,
                                        input_layouts=input_layouts,
                                        dtypes=dtypes, name=name)
        )
    if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return _result
    raise
  _result = _outputs[:]
  if not _result:
    return _op
  if _execute.must_record_gradient():
    _attrs = ("input_shapes", _op.get_attr("input_shapes"), "input_layouts",
              _op.get_attr("input_layouts"), "dtypes", _op.get_attr("dtypes"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "DTensorRestoreV2", _inputs_flat, _attrs, _result)
  return _result

DTensorRestoreV2 = tf_export("raw_ops.DTensorRestoreV2")(_ops.to_raw_op(d_tensor_restore_v2))
_dispatcher_for_d_tensor_restore_v2 = d_tensor_restore_v2._tf_type_based_dispatcher.Dispatch


def d_tensor_restore_v2_eager_fallback(prefix, tensor_names, shape_and_slices, input_shapes, input_layouts, dtypes, name, ctx):
  if not isinstance(input_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'input_shapes' argument to "
        "'d_tensor_restore_v2' Op, not %r." % input_shapes)
  input_shapes = [_execute.make_shape(_s, "input_shapes") for _s in input_shapes]
  if not isinstance(input_layouts, (list, tuple)):
    raise TypeError(
        "Expected list for 'input_layouts' argument to "
        "'d_tensor_restore_v2' Op, not %r." % input_layouts)
  input_layouts = [_execute.make_str(_s, "input_layouts") for _s in input_layouts]
  if not isinstance(dtypes, (list, tuple)):
    raise TypeError(
        "Expected list for 'dtypes' argument to "
        "'d_tensor_restore_v2' Op, not %r." % dtypes)
  dtypes = [_execute.make_type(_t, "dtypes") for _t in dtypes]
  prefix = _ops.convert_to_tensor(prefix, _dtypes.string)
  tensor_names = _ops.convert_to_tensor(tensor_names, _dtypes.string)
  shape_and_slices = _ops.convert_to_tensor(shape_and_slices, _dtypes.string)
  _inputs_flat = [prefix, tensor_names, shape_and_slices]
  _attrs = ("input_shapes", input_shapes, "input_layouts", input_layouts,
  "dtypes", dtypes)
  _result = _execute.execute(b"DTensorRestoreV2", len(dtypes),
                             inputs=_inputs_flat, attrs=_attrs, ctx=ctx,
                             name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "DTensorRestoreV2", _inputs_flat, _attrs, _result)
  return _result


@_dispatch.add_fallback_dispatch_list
@_dispatch.add_type_based_api_dispatcher
@tf_export('d_tensor_sharded_prefix')
def d_tensor_sharded_prefix(prefix, tensor_names, shape_and_slices, mesh, layouts, tensors, name=None):
  r"""TODO: add doc.

  Args:
    prefix: A `Tensor` of type `string`.
    tensor_names: A `Tensor` of type `string`.
    shape_and_slices: A `Tensor` of type `string`.
    mesh: A `Tensor` of type `string`.
    layouts: A `Tensor` of type `string`.
    tensors: A list of `Tensor` objects.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "DTensorShardedPrefix", name, prefix, tensor_names,
        shape_and_slices, mesh, layouts, tensors)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      _result = _dispatcher_for_d_tensor_sharded_prefix(
          (prefix, tensor_names, shape_and_slices, mesh, layouts, tensors,
          name,), None)
      if _result is not NotImplemented:
        return _result
      return d_tensor_sharded_prefix_eager_fallback(
          prefix, tensor_names, shape_and_slices, mesh, layouts, tensors,
          name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      _result = _dispatch.dispatch(
            d_tensor_sharded_prefix, (), dict(prefix=prefix,
                                              tensor_names=tensor_names,
                                              shape_and_slices=shape_and_slices,
                                              mesh=mesh, layouts=layouts,
                                              tensors=tensors, name=name)
          )
      if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return _result
      raise
  else:
    _result = _dispatcher_for_d_tensor_sharded_prefix(
        (prefix, tensor_names, shape_and_slices, mesh, layouts, tensors,
        name,), None)
    if _result is not NotImplemented:
      return _result
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "DTensorShardedPrefix", prefix=prefix, tensor_names=tensor_names,
                                shape_and_slices=shape_and_slices, mesh=mesh,
                                layouts=layouts, tensors=tensors, name=name)
  except (TypeError, ValueError):
    _result = _dispatch.dispatch(
          d_tensor_sharded_prefix, (), dict(prefix=prefix,
                                            tensor_names=tensor_names,
                                            shape_and_slices=shape_and_slices,
                                            mesh=mesh, layouts=layouts,
                                            tensors=tensors, name=name)
        )
    if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return _result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("dtypes", _op.get_attr("dtypes"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "DTensorShardedPrefix", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

DTensorShardedPrefix = tf_export("raw_ops.DTensorShardedPrefix")(_ops.to_raw_op(d_tensor_sharded_prefix))
_dispatcher_for_d_tensor_sharded_prefix = d_tensor_sharded_prefix._tf_type_based_dispatcher.Dispatch


def d_tensor_sharded_prefix_eager_fallback(prefix, tensor_names, shape_and_slices, mesh, layouts, tensors, name, ctx):
  _attr_dtypes, tensors = _execute.convert_to_mixed_eager_tensors(tensors, ctx)
  prefix = _ops.convert_to_tensor(prefix, _dtypes.string)
  tensor_names = _ops.convert_to_tensor(tensor_names, _dtypes.string)
  shape_and_slices = _ops.convert_to_tensor(shape_and_slices, _dtypes.string)
  mesh = _ops.convert_to_tensor(mesh, _dtypes.string)
  layouts = _ops.convert_to_tensor(layouts, _dtypes.string)
  _inputs_flat = [prefix, tensor_names, shape_and_slices, mesh, layouts] + list(tensors)
  _attrs = ("dtypes", _attr_dtypes)
  _result = _execute.execute(b"DTensorShardedPrefix", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "DTensorShardedPrefix", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_fallback_dispatch_list
@_dispatch.add_type_based_api_dispatcher
@tf_export('relayout')
def relayout(input, layout, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor`.
    layout: A `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "Relayout", name, input, "layout", layout)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      _result = _dispatcher_for_relayout(
          (input, layout, name,), None)
      if _result is not NotImplemented:
        return _result
      return relayout_eager_fallback(
          input, layout=layout, name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      _result = _dispatch.dispatch(
            relayout, (), dict(input=input, layout=layout, name=name)
          )
      if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return _result
      raise
  else:
    _result = _dispatcher_for_relayout(
        (input, layout, name,), None)
    if _result is not NotImplemented:
      return _result
  # Add nodes to the TensorFlow graph.
  layout = _execute.make_str(layout, "layout")
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Relayout", input=input, layout=layout, name=name)
  except (TypeError, ValueError):
    _result = _dispatch.dispatch(
          relayout, (), dict(input=input, layout=layout, name=name)
        )
    if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return _result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("layout", _op.get_attr("layout"), "T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "Relayout", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

Relayout = tf_export("raw_ops.Relayout")(_ops.to_raw_op(relayout))
_dispatcher_for_relayout = relayout._tf_type_based_dispatcher.Dispatch


def relayout_eager_fallback(input, layout, name, ctx):
  layout = _execute.make_str(layout, "layout")
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx, [])
  _inputs_flat = [input]
  _attrs = ("layout", layout, "T", _attr_T)
  _result = _execute.execute(b"Relayout", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "Relayout", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_fallback_dispatch_list
@_dispatch.add_type_based_api_dispatcher
@tf_export('shutdown_tpu_system')
def shutdown_tpu_system(name=None):
  r"""An op that shuts down the TPU system.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
    A boolean that indicates if the shut down process succeeds.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx, "ShutdownTPUSystem", name)
      return _result
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
    except _core._FallbackException:
      pass
    try:
      _result = _dispatcher_for_shutdown_tpu_system(
          (name,), None)
      if _result is not NotImplemented:
        return _result
      return shutdown_tpu_system_eager_fallback(
          name=name, ctx=_ctx)
    except _core._SymbolicException:
      pass  # Add nodes to the TensorFlow graph.
    except (TypeError, ValueError):
      _result = _dispatch.dispatch(
            shutdown_tpu_system, (), dict(name=name)
          )
      if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
        return _result
      raise
  else:
    _result = _dispatcher_for_shutdown_tpu_system(
        (name,), None)
    if _result is not NotImplemented:
      return _result
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "ShutdownTPUSystem", name=name)
  except (TypeError, ValueError):
    _result = _dispatch.dispatch(
          shutdown_tpu_system, (), dict(name=name)
        )
    if _result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return _result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ()
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "ShutdownTPUSystem", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

ShutdownTPUSystem = tf_export("raw_ops.ShutdownTPUSystem")(_ops.to_raw_op(shutdown_tpu_system))
_dispatcher_for_shutdown_tpu_system = shutdown_tpu_system._tf_type_based_dispatcher.Dispatch


def shutdown_tpu_system_eager_fallback(name, ctx):
  _inputs_flat = []
  _attrs = None
  _result = _execute.execute(b"ShutdownTPUSystem", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "ShutdownTPUSystem", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

