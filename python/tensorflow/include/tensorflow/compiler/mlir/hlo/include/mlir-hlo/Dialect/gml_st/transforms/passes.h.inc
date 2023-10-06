/* Autogenerated by mlir-tblgen; don't manually edit */
#ifdef GEN_PASS_CLASSES

//===----------------------------------------------------------------------===//
// GmlStToScf
//===----------------------------------------------------------------------===//

template <typename DerivedT>
class GmlStToScfBase : public ::mlir::OperationPass<mlir::func::FuncOp> {
public:
  using Base = GmlStToScfBase;

  GmlStToScfBase() : ::mlir::OperationPass<mlir::func::FuncOp>(::mlir::TypeID::get<DerivedT>()) {}
  GmlStToScfBase(const GmlStToScfBase &other) : ::mlir::OperationPass<mlir::func::FuncOp>(other) {}

  /// Returns the command-line argument attached to this pass.
  static constexpr ::llvm::StringLiteral getArgumentName() {
    return ::llvm::StringLiteral("gml-st-to-scf");
  }
  ::llvm::StringRef getArgument() const override { return "gml-st-to-scf"; }

  ::llvm::StringRef getDescription() const override { return "Lower `gml_st.loop` to SCF loops and parallel loops"; }

  /// Returns the derived pass name.
  static constexpr ::llvm::StringLiteral getPassName() {
    return ::llvm::StringLiteral("GmlStToScf");
  }
  ::llvm::StringRef getName() const override { return "GmlStToScf"; }

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
    
  registry.insert<::mlir::scf::SCFDialect>();

  }

protected:
};

//===----------------------------------------------------------------------===//
// GreedyTilingPass
//===----------------------------------------------------------------------===//

template <typename DerivedT>
class GreedyTilingPassBase : public ::mlir::OperationPass<mlir::func::FuncOp> {
public:
  using Base = GreedyTilingPassBase;

  GreedyTilingPassBase() : ::mlir::OperationPass<mlir::func::FuncOp>(::mlir::TypeID::get<DerivedT>()) {}
  GreedyTilingPassBase(const GreedyTilingPassBase &other) : ::mlir::OperationPass<mlir::func::FuncOp>(other) {}

  /// Returns the command-line argument attached to this pass.
  static constexpr ::llvm::StringLiteral getArgumentName() {
    return ::llvm::StringLiteral("gml-greedy-tiling");
  }
  ::llvm::StringRef getArgument() const override { return "gml-greedy-tiling"; }

  ::llvm::StringRef getDescription() const override { return "Tile producers of gml_st.materialize operations"; }

  /// Returns the derived pass name.
  static constexpr ::llvm::StringLiteral getPassName() {
    return ::llvm::StringLiteral("GreedyTilingPass");
  }
  ::llvm::StringRef getName() const override { return "GreedyTilingPass"; }

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
// GmlStToScf Registration
//===----------------------------------------------------------------------===//

inline void registerGmlStToScfPass() {
  ::mlir::registerPass([]() -> std::unique_ptr<::mlir::Pass> {
    return ::mlir::gml_st::createGmlStToScfPass();
  });
}

//===----------------------------------------------------------------------===//
// GreedyTilingPass Registration
//===----------------------------------------------------------------------===//

inline void registerGreedyTilingPassPass() {
  ::mlir::registerPass([]() -> std::unique_ptr<::mlir::Pass> {
    return ::mlir::gml_st::createGreedyTilingPass();
  });
}

//===----------------------------------------------------------------------===//
// GmlSt Registration
//===----------------------------------------------------------------------===//

inline void registerGmlStPasses() {
  registerGmlStToScfPass();
  registerGreedyTilingPassPass();
}
#undef GEN_PASS_REGISTRATION
#endif // GEN_PASS_REGISTRATION