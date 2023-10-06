/* Autogenerated by mlir-tblgen; don't manually edit */
#ifdef GEN_PASS_CLASSES

//===----------------------------------------------------------------------===//
// ArithmeticBufferize
//===----------------------------------------------------------------------===//

template <typename DerivedT>
class ArithmeticBufferizeBase : public ::mlir::OperationPass<ModuleOp> {
public:
  using Base = ArithmeticBufferizeBase;

  ArithmeticBufferizeBase() : ::mlir::OperationPass<ModuleOp>(::mlir::TypeID::get<DerivedT>()) {}
  ArithmeticBufferizeBase(const ArithmeticBufferizeBase &other) : ::mlir::OperationPass<ModuleOp>(other) {}

  /// Returns the command-line argument attached to this pass.
  static constexpr ::llvm::StringLiteral getArgumentName() {
    return ::llvm::StringLiteral("arith-bufferize");
  }
  ::llvm::StringRef getArgument() const override { return "arith-bufferize"; }

  ::llvm::StringRef getDescription() const override { return "Bufferize Arithmetic dialect ops."; }

  /// Returns the derived pass name.
  static constexpr ::llvm::StringLiteral getPassName() {
    return ::llvm::StringLiteral("ArithmeticBufferize");
  }
  ::llvm::StringRef getName() const override { return "ArithmeticBufferize"; }

  /// Support isa/dyn_cast functionality for the derived pass class.
  static bool classof(const ::mlir::Pass *pass) {
    return pass->getTypeID() == ::mlir::TypeID::get<DerivedT>();
  }

  /// A clone method to create a copy of this pass.
  std::unique_ptr<::mlir::Pass> clonePass() const override {
    return std::make_unique<DerivedT>(*static_cast<const DerivedT *>(this));
  }

  /// Return the dialect that must be loaded in the context before this pass.
  void getDependentDialects(::mlir::DialectRegistry &registry) const override {
    
  }

protected:
  ::mlir::Pass::Option<unsigned> alignment{*this, "alignment", ::llvm::cl::desc("Create global memrefs with a specified alignment"), ::llvm::cl::init(0)};
};

//===----------------------------------------------------------------------===//
// ArithmeticExpandOps
//===----------------------------------------------------------------------===//

template <typename DerivedT>
class ArithmeticExpandOpsBase : public ::mlir::OperationPass<> {
public:
  using Base = ArithmeticExpandOpsBase;

  ArithmeticExpandOpsBase() : ::mlir::OperationPass<>(::mlir::TypeID::get<DerivedT>()) {}
  ArithmeticExpandOpsBase(const ArithmeticExpandOpsBase &other) : ::mlir::OperationPass<>(other) {}

  /// Returns the command-line argument attached to this pass.
  static constexpr ::llvm::StringLiteral getArgumentName() {
    return ::llvm::StringLiteral("arith-expand");
  }
  ::llvm::StringRef getArgument() const override { return "arith-expand"; }

  ::llvm::StringRef getDescription() const override { return "Legalize Arithmetic ops to be convertible to LLVM."; }

  /// Returns the derived pass name.
  static constexpr ::llvm::StringLiteral getPassName() {
    return ::llvm::StringLiteral("ArithmeticExpandOps");
  }
  ::llvm::StringRef getName() const override { return "ArithmeticExpandOps"; }

  /// Support isa/dyn_cast functionality for the derived pass class.
  static bool classof(const ::mlir::Pass *pass) {
    return pass->getTypeID() == ::mlir::TypeID::get<DerivedT>();
  }

  /// A clone method to create a copy of this pass.
  std::unique_ptr<::mlir::Pass> clonePass() const override {
    return std::make_unique<DerivedT>(*static_cast<const DerivedT *>(this));
  }

  /// Return the dialect that must be loaded in the context before this pass.
  void getDependentDialects(::mlir::DialectRegistry &registry) const override {
    
  }

protected:
};
#undef GEN_PASS_CLASSES
#endif // GEN_PASS_CLASSES
#ifdef GEN_PASS_REGISTRATION

//===----------------------------------------------------------------------===//
// ArithmeticBufferize Registration
//===----------------------------------------------------------------------===//

inline void registerArithmeticBufferizePass() {
  ::mlir::registerPass([]() -> std::unique_ptr<::mlir::Pass> {
    return mlir::arith::createArithmeticBufferizePass();
  });
}

//===----------------------------------------------------------------------===//
// ArithmeticExpandOps Registration
//===----------------------------------------------------------------------===//

inline void registerArithmeticExpandOpsPass() {
  ::mlir::registerPass([]() -> std::unique_ptr<::mlir::Pass> {
    return mlir::arith::createArithmeticExpandOpsPass();
  });
}

//===----------------------------------------------------------------------===//
// Arithmetic Registration
//===----------------------------------------------------------------------===//

inline void registerArithmeticPasses() {
  registerArithmeticBufferizePass();
  registerArithmeticExpandOpsPass();
}
#undef GEN_PASS_REGISTRATION
#endif // GEN_PASS_REGISTRATION