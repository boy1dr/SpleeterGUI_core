/* Autogenerated by mlir-tblgen; don't manually edit. */
//===----------------------------------------------------------------------===//
// SparseTensor Group Registration
//===----------------------------------------------------------------------===//

void mlirRegisterSparseTensorPasses() {
  registerSparseTensorPasses();
}

MlirPass mlirCreateSparseTensorSparseTensorConversion() {
  return wrap(mlir::createSparseTensorConversionPass().release());
}
void mlirRegisterSparseTensorSparseTensorConversion() {
  registerSparseTensorConversionPass();
}


MlirPass mlirCreateSparseTensorSparsification() {
  return wrap(mlir::createSparsificationPass().release());
}
void mlirRegisterSparseTensorSparsification() {
  registerSparsificationPass();
}
