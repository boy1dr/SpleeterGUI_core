// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: tensorflow/compiler/xla/service/gpu/backend_configs.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3009000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3009002 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
#include "tensorflow/compiler/xla/xla_data.pb.h"
#include "tensorflow/stream_executor/dnn.pb.h"
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto {
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::AuxillaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTable schema[3]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::FieldMetadata field_metadata[];
  static const ::PROTOBUF_NAMESPACE_ID::internal::SerializationTable serialization_table[];
  static const ::PROTOBUF_NAMESPACE_ID::uint32 offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto;
namespace xla {
namespace gpu {
class BitcastBackendConfig;
class BitcastBackendConfigDefaultTypeInternal;
extern BitcastBackendConfigDefaultTypeInternal _BitcastBackendConfig_default_instance_;
class CudnnConvBackendConfig;
class CudnnConvBackendConfigDefaultTypeInternal;
extern CudnnConvBackendConfigDefaultTypeInternal _CudnnConvBackendConfig_default_instance_;
class GemmBackendConfig;
class GemmBackendConfigDefaultTypeInternal;
extern GemmBackendConfigDefaultTypeInternal _GemmBackendConfig_default_instance_;
}  // namespace gpu
}  // namespace xla
PROTOBUF_NAMESPACE_OPEN
template<> ::xla::gpu::BitcastBackendConfig* Arena::CreateMaybeMessage<::xla::gpu::BitcastBackendConfig>(Arena*);
template<> ::xla::gpu::CudnnConvBackendConfig* Arena::CreateMaybeMessage<::xla::gpu::CudnnConvBackendConfig>(Arena*);
template<> ::xla::gpu::GemmBackendConfig* Arena::CreateMaybeMessage<::xla::gpu::GemmBackendConfig>(Arena*);
PROTOBUF_NAMESPACE_CLOSE
namespace xla {
namespace gpu {

// ===================================================================

class CudnnConvBackendConfig :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:xla.gpu.CudnnConvBackendConfig) */ {
 public:
  CudnnConvBackendConfig();
  virtual ~CudnnConvBackendConfig();

  CudnnConvBackendConfig(const CudnnConvBackendConfig& from);
  CudnnConvBackendConfig(CudnnConvBackendConfig&& from) noexcept
    : CudnnConvBackendConfig() {
    *this = ::std::move(from);
  }

  inline CudnnConvBackendConfig& operator=(const CudnnConvBackendConfig& from) {
    CopyFrom(from);
    return *this;
  }
  inline CudnnConvBackendConfig& operator=(CudnnConvBackendConfig&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const CudnnConvBackendConfig& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const CudnnConvBackendConfig* internal_default_instance() {
    return reinterpret_cast<const CudnnConvBackendConfig*>(
               &_CudnnConvBackendConfig_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  friend void swap(CudnnConvBackendConfig& a, CudnnConvBackendConfig& b) {
    a.Swap(&b);
  }
  inline void Swap(CudnnConvBackendConfig* other) {
    if (other == this) return;
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline CudnnConvBackendConfig* New() const final {
    return CreateMaybeMessage<CudnnConvBackendConfig>(nullptr);
  }

  CudnnConvBackendConfig* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<CudnnConvBackendConfig>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const CudnnConvBackendConfig& from);
  void MergeFrom(const CudnnConvBackendConfig& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  #else
  bool MergePartialFromCodedStream(
      ::PROTOBUF_NAMESPACE_ID::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::PROTOBUF_NAMESPACE_ID::io::CodedOutputStream* output) const final;
  ::PROTOBUF_NAMESPACE_ID::uint8* InternalSerializeWithCachedSizesToArray(
      ::PROTOBUF_NAMESPACE_ID::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(CudnnConvBackendConfig* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "xla.gpu.CudnnConvBackendConfig";
  }
  private:
  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto);
    return ::descriptor_table_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kAlgorithmFieldNumber = 6,
    kActivationModeFieldNumber = 3,
    kConvResultScaleFieldNumber = 4,
    kSideInputScaleFieldNumber = 5,
  };
  // .stream_executor.dnn.AlgorithmProto algorithm = 6;
  bool has_algorithm() const;
  void clear_algorithm();
  const ::stream_executor::dnn::AlgorithmProto& algorithm() const;
  ::stream_executor::dnn::AlgorithmProto* release_algorithm();
  ::stream_executor::dnn::AlgorithmProto* mutable_algorithm();
  void set_allocated_algorithm(::stream_executor::dnn::AlgorithmProto* algorithm);

  // int64 activation_mode = 3;
  void clear_activation_mode();
  ::PROTOBUF_NAMESPACE_ID::int64 activation_mode() const;
  void set_activation_mode(::PROTOBUF_NAMESPACE_ID::int64 value);

  // double conv_result_scale = 4;
  void clear_conv_result_scale();
  double conv_result_scale() const;
  void set_conv_result_scale(double value);

  // double side_input_scale = 5;
  void clear_side_input_scale();
  double side_input_scale() const;
  void set_side_input_scale(double value);

  // @@protoc_insertion_point(class_scope:xla.gpu.CudnnConvBackendConfig)
 private:
  class _Internal;

  ::PROTOBUF_NAMESPACE_ID::internal::InternalMetadataWithArena _internal_metadata_;
  ::stream_executor::dnn::AlgorithmProto* algorithm_;
  ::PROTOBUF_NAMESPACE_ID::int64 activation_mode_;
  double conv_result_scale_;
  double side_input_scale_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto;
};
// -------------------------------------------------------------------

class GemmBackendConfig :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:xla.gpu.GemmBackendConfig) */ {
 public:
  GemmBackendConfig();
  virtual ~GemmBackendConfig();

  GemmBackendConfig(const GemmBackendConfig& from);
  GemmBackendConfig(GemmBackendConfig&& from) noexcept
    : GemmBackendConfig() {
    *this = ::std::move(from);
  }

  inline GemmBackendConfig& operator=(const GemmBackendConfig& from) {
    CopyFrom(from);
    return *this;
  }
  inline GemmBackendConfig& operator=(GemmBackendConfig&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const GemmBackendConfig& default_instance();

  enum AlgorithmCase {
    kSelectedAlgorithm = 1,
    ALGORITHM_NOT_SET = 0,
  };

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const GemmBackendConfig* internal_default_instance() {
    return reinterpret_cast<const GemmBackendConfig*>(
               &_GemmBackendConfig_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  friend void swap(GemmBackendConfig& a, GemmBackendConfig& b) {
    a.Swap(&b);
  }
  inline void Swap(GemmBackendConfig* other) {
    if (other == this) return;
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline GemmBackendConfig* New() const final {
    return CreateMaybeMessage<GemmBackendConfig>(nullptr);
  }

  GemmBackendConfig* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<GemmBackendConfig>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const GemmBackendConfig& from);
  void MergeFrom(const GemmBackendConfig& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  #else
  bool MergePartialFromCodedStream(
      ::PROTOBUF_NAMESPACE_ID::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::PROTOBUF_NAMESPACE_ID::io::CodedOutputStream* output) const final;
  ::PROTOBUF_NAMESPACE_ID::uint8* InternalSerializeWithCachedSizesToArray(
      ::PROTOBUF_NAMESPACE_ID::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(GemmBackendConfig* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "xla.gpu.GemmBackendConfig";
  }
  private:
  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto);
    return ::descriptor_table_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kDotDimensionNumbersFieldNumber = 7,
    kAlphaRealFieldNumber = 2,
    kBetaFieldNumber = 3,
    kBatchSizeFieldNumber = 8,
    kAlphaImagFieldNumber = 9,
    kLhsStrideFieldNumber = 10,
    kRhsStrideFieldNumber = 11,
    kSelectedAlgorithmFieldNumber = 1,
  };
  // .xla.DotDimensionNumbers dot_dimension_numbers = 7;
  bool has_dot_dimension_numbers() const;
  void clear_dot_dimension_numbers();
  const ::xla::DotDimensionNumbers& dot_dimension_numbers() const;
  ::xla::DotDimensionNumbers* release_dot_dimension_numbers();
  ::xla::DotDimensionNumbers* mutable_dot_dimension_numbers();
  void set_allocated_dot_dimension_numbers(::xla::DotDimensionNumbers* dot_dimension_numbers);

  // double alpha_real = 2;
  void clear_alpha_real();
  double alpha_real() const;
  void set_alpha_real(double value);

  // double beta = 3;
  void clear_beta();
  double beta() const;
  void set_beta(double value);

  // int64 batch_size = 8;
  void clear_batch_size();
  ::PROTOBUF_NAMESPACE_ID::int64 batch_size() const;
  void set_batch_size(::PROTOBUF_NAMESPACE_ID::int64 value);

  // double alpha_imag = 9;
  void clear_alpha_imag();
  double alpha_imag() const;
  void set_alpha_imag(double value);

  // int64 lhs_stride = 10;
  void clear_lhs_stride();
  ::PROTOBUF_NAMESPACE_ID::int64 lhs_stride() const;
  void set_lhs_stride(::PROTOBUF_NAMESPACE_ID::int64 value);

  // int64 rhs_stride = 11;
  void clear_rhs_stride();
  ::PROTOBUF_NAMESPACE_ID::int64 rhs_stride() const;
  void set_rhs_stride(::PROTOBUF_NAMESPACE_ID::int64 value);

  // int64 selected_algorithm = 1;
  private:
  bool has_selected_algorithm() const;
  public:
  void clear_selected_algorithm();
  ::PROTOBUF_NAMESPACE_ID::int64 selected_algorithm() const;
  void set_selected_algorithm(::PROTOBUF_NAMESPACE_ID::int64 value);

  void clear_algorithm();
  AlgorithmCase algorithm_case() const;
  // @@protoc_insertion_point(class_scope:xla.gpu.GemmBackendConfig)
 private:
  class _Internal;
  void set_has_selected_algorithm();

  inline bool has_algorithm() const;
  inline void clear_has_algorithm();

  ::PROTOBUF_NAMESPACE_ID::internal::InternalMetadataWithArena _internal_metadata_;
  ::xla::DotDimensionNumbers* dot_dimension_numbers_;
  double alpha_real_;
  double beta_;
  ::PROTOBUF_NAMESPACE_ID::int64 batch_size_;
  double alpha_imag_;
  ::PROTOBUF_NAMESPACE_ID::int64 lhs_stride_;
  ::PROTOBUF_NAMESPACE_ID::int64 rhs_stride_;
  union AlgorithmUnion {
    AlgorithmUnion() {}
    ::PROTOBUF_NAMESPACE_ID::int64 selected_algorithm_;
  } algorithm_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  ::PROTOBUF_NAMESPACE_ID::uint32 _oneof_case_[1];

  friend struct ::TableStruct_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto;
};
// -------------------------------------------------------------------

class BitcastBackendConfig :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:xla.gpu.BitcastBackendConfig) */ {
 public:
  BitcastBackendConfig();
  virtual ~BitcastBackendConfig();

  BitcastBackendConfig(const BitcastBackendConfig& from);
  BitcastBackendConfig(BitcastBackendConfig&& from) noexcept
    : BitcastBackendConfig() {
    *this = ::std::move(from);
  }

  inline BitcastBackendConfig& operator=(const BitcastBackendConfig& from) {
    CopyFrom(from);
    return *this;
  }
  inline BitcastBackendConfig& operator=(BitcastBackendConfig&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const BitcastBackendConfig& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const BitcastBackendConfig* internal_default_instance() {
    return reinterpret_cast<const BitcastBackendConfig*>(
               &_BitcastBackendConfig_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    2;

  friend void swap(BitcastBackendConfig& a, BitcastBackendConfig& b) {
    a.Swap(&b);
  }
  inline void Swap(BitcastBackendConfig* other) {
    if (other == this) return;
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline BitcastBackendConfig* New() const final {
    return CreateMaybeMessage<BitcastBackendConfig>(nullptr);
  }

  BitcastBackendConfig* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<BitcastBackendConfig>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const BitcastBackendConfig& from);
  void MergeFrom(const BitcastBackendConfig& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  #else
  bool MergePartialFromCodedStream(
      ::PROTOBUF_NAMESPACE_ID::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::PROTOBUF_NAMESPACE_ID::io::CodedOutputStream* output) const final;
  ::PROTOBUF_NAMESPACE_ID::uint8* InternalSerializeWithCachedSizesToArray(
      ::PROTOBUF_NAMESPACE_ID::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(BitcastBackendConfig* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "xla.gpu.BitcastBackendConfig";
  }
  private:
  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto);
    return ::descriptor_table_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kSourceLayoutFieldNumber = 1,
    kResultLayoutFieldNumber = 2,
  };
  // .xla.LayoutProto source_layout = 1;
  bool has_source_layout() const;
  void clear_source_layout();
  const ::xla::LayoutProto& source_layout() const;
  ::xla::LayoutProto* release_source_layout();
  ::xla::LayoutProto* mutable_source_layout();
  void set_allocated_source_layout(::xla::LayoutProto* source_layout);

  // .xla.LayoutProto result_layout = 2;
  bool has_result_layout() const;
  void clear_result_layout();
  const ::xla::LayoutProto& result_layout() const;
  ::xla::LayoutProto* release_result_layout();
  ::xla::LayoutProto* mutable_result_layout();
  void set_allocated_result_layout(::xla::LayoutProto* result_layout);

  // @@protoc_insertion_point(class_scope:xla.gpu.BitcastBackendConfig)
 private:
  class _Internal;

  ::PROTOBUF_NAMESPACE_ID::internal::InternalMetadataWithArena _internal_metadata_;
  ::xla::LayoutProto* source_layout_;
  ::xla::LayoutProto* result_layout_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// CudnnConvBackendConfig

// .stream_executor.dnn.AlgorithmProto algorithm = 6;
inline bool CudnnConvBackendConfig::has_algorithm() const {
  return this != internal_default_instance() && algorithm_ != nullptr;
}
inline const ::stream_executor::dnn::AlgorithmProto& CudnnConvBackendConfig::algorithm() const {
  const ::stream_executor::dnn::AlgorithmProto* p = algorithm_;
  // @@protoc_insertion_point(field_get:xla.gpu.CudnnConvBackendConfig.algorithm)
  return p != nullptr ? *p : *reinterpret_cast<const ::stream_executor::dnn::AlgorithmProto*>(
      &::stream_executor::dnn::_AlgorithmProto_default_instance_);
}
inline ::stream_executor::dnn::AlgorithmProto* CudnnConvBackendConfig::release_algorithm() {
  // @@protoc_insertion_point(field_release:xla.gpu.CudnnConvBackendConfig.algorithm)
  
  ::stream_executor::dnn::AlgorithmProto* temp = algorithm_;
  algorithm_ = nullptr;
  return temp;
}
inline ::stream_executor::dnn::AlgorithmProto* CudnnConvBackendConfig::mutable_algorithm() {
  
  if (algorithm_ == nullptr) {
    auto* p = CreateMaybeMessage<::stream_executor::dnn::AlgorithmProto>(GetArenaNoVirtual());
    algorithm_ = p;
  }
  // @@protoc_insertion_point(field_mutable:xla.gpu.CudnnConvBackendConfig.algorithm)
  return algorithm_;
}
inline void CudnnConvBackendConfig::set_allocated_algorithm(::stream_executor::dnn::AlgorithmProto* algorithm) {
  ::PROTOBUF_NAMESPACE_ID::Arena* message_arena = GetArenaNoVirtual();
  if (message_arena == nullptr) {
    delete reinterpret_cast< ::PROTOBUF_NAMESPACE_ID::MessageLite*>(algorithm_);
  }
  if (algorithm) {
    ::PROTOBUF_NAMESPACE_ID::Arena* submessage_arena = nullptr;
    if (message_arena != submessage_arena) {
      algorithm = ::PROTOBUF_NAMESPACE_ID::internal::GetOwnedMessage(
          message_arena, algorithm, submessage_arena);
    }
    
  } else {
    
  }
  algorithm_ = algorithm;
  // @@protoc_insertion_point(field_set_allocated:xla.gpu.CudnnConvBackendConfig.algorithm)
}

// double conv_result_scale = 4;
inline void CudnnConvBackendConfig::clear_conv_result_scale() {
  conv_result_scale_ = 0;
}
inline double CudnnConvBackendConfig::conv_result_scale() const {
  // @@protoc_insertion_point(field_get:xla.gpu.CudnnConvBackendConfig.conv_result_scale)
  return conv_result_scale_;
}
inline void CudnnConvBackendConfig::set_conv_result_scale(double value) {
  
  conv_result_scale_ = value;
  // @@protoc_insertion_point(field_set:xla.gpu.CudnnConvBackendConfig.conv_result_scale)
}

// int64 activation_mode = 3;
inline void CudnnConvBackendConfig::clear_activation_mode() {
  activation_mode_ = PROTOBUF_LONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::int64 CudnnConvBackendConfig::activation_mode() const {
  // @@protoc_insertion_point(field_get:xla.gpu.CudnnConvBackendConfig.activation_mode)
  return activation_mode_;
}
inline void CudnnConvBackendConfig::set_activation_mode(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  activation_mode_ = value;
  // @@protoc_insertion_point(field_set:xla.gpu.CudnnConvBackendConfig.activation_mode)
}

// double side_input_scale = 5;
inline void CudnnConvBackendConfig::clear_side_input_scale() {
  side_input_scale_ = 0;
}
inline double CudnnConvBackendConfig::side_input_scale() const {
  // @@protoc_insertion_point(field_get:xla.gpu.CudnnConvBackendConfig.side_input_scale)
  return side_input_scale_;
}
inline void CudnnConvBackendConfig::set_side_input_scale(double value) {
  
  side_input_scale_ = value;
  // @@protoc_insertion_point(field_set:xla.gpu.CudnnConvBackendConfig.side_input_scale)
}

// -------------------------------------------------------------------

// GemmBackendConfig

// int64 selected_algorithm = 1;
inline bool GemmBackendConfig::has_selected_algorithm() const {
  return algorithm_case() == kSelectedAlgorithm;
}
inline void GemmBackendConfig::set_has_selected_algorithm() {
  _oneof_case_[0] = kSelectedAlgorithm;
}
inline void GemmBackendConfig::clear_selected_algorithm() {
  if (has_selected_algorithm()) {
    algorithm_.selected_algorithm_ = PROTOBUF_LONGLONG(0);
    clear_has_algorithm();
  }
}
inline ::PROTOBUF_NAMESPACE_ID::int64 GemmBackendConfig::selected_algorithm() const {
  // @@protoc_insertion_point(field_get:xla.gpu.GemmBackendConfig.selected_algorithm)
  if (has_selected_algorithm()) {
    return algorithm_.selected_algorithm_;
  }
  return PROTOBUF_LONGLONG(0);
}
inline void GemmBackendConfig::set_selected_algorithm(::PROTOBUF_NAMESPACE_ID::int64 value) {
  if (!has_selected_algorithm()) {
    clear_algorithm();
    set_has_selected_algorithm();
  }
  algorithm_.selected_algorithm_ = value;
  // @@protoc_insertion_point(field_set:xla.gpu.GemmBackendConfig.selected_algorithm)
}

// double alpha_real = 2;
inline void GemmBackendConfig::clear_alpha_real() {
  alpha_real_ = 0;
}
inline double GemmBackendConfig::alpha_real() const {
  // @@protoc_insertion_point(field_get:xla.gpu.GemmBackendConfig.alpha_real)
  return alpha_real_;
}
inline void GemmBackendConfig::set_alpha_real(double value) {
  
  alpha_real_ = value;
  // @@protoc_insertion_point(field_set:xla.gpu.GemmBackendConfig.alpha_real)
}

// double alpha_imag = 9;
inline void GemmBackendConfig::clear_alpha_imag() {
  alpha_imag_ = 0;
}
inline double GemmBackendConfig::alpha_imag() const {
  // @@protoc_insertion_point(field_get:xla.gpu.GemmBackendConfig.alpha_imag)
  return alpha_imag_;
}
inline void GemmBackendConfig::set_alpha_imag(double value) {
  
  alpha_imag_ = value;
  // @@protoc_insertion_point(field_set:xla.gpu.GemmBackendConfig.alpha_imag)
}

// double beta = 3;
inline void GemmBackendConfig::clear_beta() {
  beta_ = 0;
}
inline double GemmBackendConfig::beta() const {
  // @@protoc_insertion_point(field_get:xla.gpu.GemmBackendConfig.beta)
  return beta_;
}
inline void GemmBackendConfig::set_beta(double value) {
  
  beta_ = value;
  // @@protoc_insertion_point(field_set:xla.gpu.GemmBackendConfig.beta)
}

// .xla.DotDimensionNumbers dot_dimension_numbers = 7;
inline bool GemmBackendConfig::has_dot_dimension_numbers() const {
  return this != internal_default_instance() && dot_dimension_numbers_ != nullptr;
}
inline const ::xla::DotDimensionNumbers& GemmBackendConfig::dot_dimension_numbers() const {
  const ::xla::DotDimensionNumbers* p = dot_dimension_numbers_;
  // @@protoc_insertion_point(field_get:xla.gpu.GemmBackendConfig.dot_dimension_numbers)
  return p != nullptr ? *p : *reinterpret_cast<const ::xla::DotDimensionNumbers*>(
      &::xla::_DotDimensionNumbers_default_instance_);
}
inline ::xla::DotDimensionNumbers* GemmBackendConfig::release_dot_dimension_numbers() {
  // @@protoc_insertion_point(field_release:xla.gpu.GemmBackendConfig.dot_dimension_numbers)
  
  ::xla::DotDimensionNumbers* temp = dot_dimension_numbers_;
  dot_dimension_numbers_ = nullptr;
  return temp;
}
inline ::xla::DotDimensionNumbers* GemmBackendConfig::mutable_dot_dimension_numbers() {
  
  if (dot_dimension_numbers_ == nullptr) {
    auto* p = CreateMaybeMessage<::xla::DotDimensionNumbers>(GetArenaNoVirtual());
    dot_dimension_numbers_ = p;
  }
  // @@protoc_insertion_point(field_mutable:xla.gpu.GemmBackendConfig.dot_dimension_numbers)
  return dot_dimension_numbers_;
}
inline void GemmBackendConfig::set_allocated_dot_dimension_numbers(::xla::DotDimensionNumbers* dot_dimension_numbers) {
  ::PROTOBUF_NAMESPACE_ID::Arena* message_arena = GetArenaNoVirtual();
  if (message_arena == nullptr) {
    delete reinterpret_cast< ::PROTOBUF_NAMESPACE_ID::MessageLite*>(dot_dimension_numbers_);
  }
  if (dot_dimension_numbers) {
    ::PROTOBUF_NAMESPACE_ID::Arena* submessage_arena =
      reinterpret_cast<::PROTOBUF_NAMESPACE_ID::MessageLite*>(dot_dimension_numbers)->GetArena();
    if (message_arena != submessage_arena) {
      dot_dimension_numbers = ::PROTOBUF_NAMESPACE_ID::internal::GetOwnedMessage(
          message_arena, dot_dimension_numbers, submessage_arena);
    }
    
  } else {
    
  }
  dot_dimension_numbers_ = dot_dimension_numbers;
  // @@protoc_insertion_point(field_set_allocated:xla.gpu.GemmBackendConfig.dot_dimension_numbers)
}

// int64 batch_size = 8;
inline void GemmBackendConfig::clear_batch_size() {
  batch_size_ = PROTOBUF_LONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::int64 GemmBackendConfig::batch_size() const {
  // @@protoc_insertion_point(field_get:xla.gpu.GemmBackendConfig.batch_size)
  return batch_size_;
}
inline void GemmBackendConfig::set_batch_size(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  batch_size_ = value;
  // @@protoc_insertion_point(field_set:xla.gpu.GemmBackendConfig.batch_size)
}

// int64 lhs_stride = 10;
inline void GemmBackendConfig::clear_lhs_stride() {
  lhs_stride_ = PROTOBUF_LONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::int64 GemmBackendConfig::lhs_stride() const {
  // @@protoc_insertion_point(field_get:xla.gpu.GemmBackendConfig.lhs_stride)
  return lhs_stride_;
}
inline void GemmBackendConfig::set_lhs_stride(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  lhs_stride_ = value;
  // @@protoc_insertion_point(field_set:xla.gpu.GemmBackendConfig.lhs_stride)
}

// int64 rhs_stride = 11;
inline void GemmBackendConfig::clear_rhs_stride() {
  rhs_stride_ = PROTOBUF_LONGLONG(0);
}
inline ::PROTOBUF_NAMESPACE_ID::int64 GemmBackendConfig::rhs_stride() const {
  // @@protoc_insertion_point(field_get:xla.gpu.GemmBackendConfig.rhs_stride)
  return rhs_stride_;
}
inline void GemmBackendConfig::set_rhs_stride(::PROTOBUF_NAMESPACE_ID::int64 value) {
  
  rhs_stride_ = value;
  // @@protoc_insertion_point(field_set:xla.gpu.GemmBackendConfig.rhs_stride)
}

inline bool GemmBackendConfig::has_algorithm() const {
  return algorithm_case() != ALGORITHM_NOT_SET;
}
inline void GemmBackendConfig::clear_has_algorithm() {
  _oneof_case_[0] = ALGORITHM_NOT_SET;
}
inline GemmBackendConfig::AlgorithmCase GemmBackendConfig::algorithm_case() const {
  return GemmBackendConfig::AlgorithmCase(_oneof_case_[0]);
}
// -------------------------------------------------------------------

// BitcastBackendConfig

// .xla.LayoutProto source_layout = 1;
inline bool BitcastBackendConfig::has_source_layout() const {
  return this != internal_default_instance() && source_layout_ != nullptr;
}
inline const ::xla::LayoutProto& BitcastBackendConfig::source_layout() const {
  const ::xla::LayoutProto* p = source_layout_;
  // @@protoc_insertion_point(field_get:xla.gpu.BitcastBackendConfig.source_layout)
  return p != nullptr ? *p : *reinterpret_cast<const ::xla::LayoutProto*>(
      &::xla::_LayoutProto_default_instance_);
}
inline ::xla::LayoutProto* BitcastBackendConfig::release_source_layout() {
  // @@protoc_insertion_point(field_release:xla.gpu.BitcastBackendConfig.source_layout)
  
  ::xla::LayoutProto* temp = source_layout_;
  source_layout_ = nullptr;
  return temp;
}
inline ::xla::LayoutProto* BitcastBackendConfig::mutable_source_layout() {
  
  if (source_layout_ == nullptr) {
    auto* p = CreateMaybeMessage<::xla::LayoutProto>(GetArenaNoVirtual());
    source_layout_ = p;
  }
  // @@protoc_insertion_point(field_mutable:xla.gpu.BitcastBackendConfig.source_layout)
  return source_layout_;
}
inline void BitcastBackendConfig::set_allocated_source_layout(::xla::LayoutProto* source_layout) {
  ::PROTOBUF_NAMESPACE_ID::Arena* message_arena = GetArenaNoVirtual();
  if (message_arena == nullptr) {
    delete reinterpret_cast< ::PROTOBUF_NAMESPACE_ID::MessageLite*>(source_layout_);
  }
  if (source_layout) {
    ::PROTOBUF_NAMESPACE_ID::Arena* submessage_arena =
      reinterpret_cast<::PROTOBUF_NAMESPACE_ID::MessageLite*>(source_layout)->GetArena();
    if (message_arena != submessage_arena) {
      source_layout = ::PROTOBUF_NAMESPACE_ID::internal::GetOwnedMessage(
          message_arena, source_layout, submessage_arena);
    }
    
  } else {
    
  }
  source_layout_ = source_layout;
  // @@protoc_insertion_point(field_set_allocated:xla.gpu.BitcastBackendConfig.source_layout)
}

// .xla.LayoutProto result_layout = 2;
inline bool BitcastBackendConfig::has_result_layout() const {
  return this != internal_default_instance() && result_layout_ != nullptr;
}
inline const ::xla::LayoutProto& BitcastBackendConfig::result_layout() const {
  const ::xla::LayoutProto* p = result_layout_;
  // @@protoc_insertion_point(field_get:xla.gpu.BitcastBackendConfig.result_layout)
  return p != nullptr ? *p : *reinterpret_cast<const ::xla::LayoutProto*>(
      &::xla::_LayoutProto_default_instance_);
}
inline ::xla::LayoutProto* BitcastBackendConfig::release_result_layout() {
  // @@protoc_insertion_point(field_release:xla.gpu.BitcastBackendConfig.result_layout)
  
  ::xla::LayoutProto* temp = result_layout_;
  result_layout_ = nullptr;
  return temp;
}
inline ::xla::LayoutProto* BitcastBackendConfig::mutable_result_layout() {
  
  if (result_layout_ == nullptr) {
    auto* p = CreateMaybeMessage<::xla::LayoutProto>(GetArenaNoVirtual());
    result_layout_ = p;
  }
  // @@protoc_insertion_point(field_mutable:xla.gpu.BitcastBackendConfig.result_layout)
  return result_layout_;
}
inline void BitcastBackendConfig::set_allocated_result_layout(::xla::LayoutProto* result_layout) {
  ::PROTOBUF_NAMESPACE_ID::Arena* message_arena = GetArenaNoVirtual();
  if (message_arena == nullptr) {
    delete reinterpret_cast< ::PROTOBUF_NAMESPACE_ID::MessageLite*>(result_layout_);
  }
  if (result_layout) {
    ::PROTOBUF_NAMESPACE_ID::Arena* submessage_arena =
      reinterpret_cast<::PROTOBUF_NAMESPACE_ID::MessageLite*>(result_layout)->GetArena();
    if (message_arena != submessage_arena) {
      result_layout = ::PROTOBUF_NAMESPACE_ID::internal::GetOwnedMessage(
          message_arena, result_layout, submessage_arena);
    }
    
  } else {
    
  }
  result_layout_ = result_layout;
  // @@protoc_insertion_point(field_set_allocated:xla.gpu.BitcastBackendConfig.result_layout)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------

// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace gpu
}  // namespace xla

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcompiler_2fxla_2fservice_2fgpu_2fbackend_5fconfigs_2eproto