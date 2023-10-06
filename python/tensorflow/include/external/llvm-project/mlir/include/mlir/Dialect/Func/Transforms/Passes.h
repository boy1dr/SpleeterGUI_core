//===- Passes.h - Pass Entrypoints ------------------------------*- C++ -*-===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//
//
// This header file defines prototypes that expose pass constructors in the Func
// transformation library.
//
//===----------------------------------------------------------------------===//

#ifndef MLIR_DIALECT_FUNC_TRANSFORMS_PASSES_H
#define MLIR_DIALECT_FUNC_TRANSFORMS_PASSES_H

#include "mlir/Pass/Pass.h"

namespace mlir {
namespace bufferization {
class BufferizeTypeConverter;
} // namespace bufferization

class RewritePatternSet;

namespace func {
/// Creates an instance of func bufferization pass.
std::unique_ptr<Pass> createFuncBufferizePass();

//===----------------------------------------------------------------------===//
// Registration
//===----------------------------------------------------------------------===//

/// Generate the code for registering passes.
#define GEN_PASS_REGISTRATION
#include "mlir/Dialect/Func/Transforms/Passes.h.inc"

} // namespace func
} // namespace mlir

#endif // MLIR_DIALECT_FUNC_TRANSFORMS_PASSES_H
