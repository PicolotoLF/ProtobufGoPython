// Code generated by protoc-gen-go. DO NOT EDIT.
// source: requests_mercadolibre.proto

package api

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type PingMessage struct {
	Greeting             string   `protobuf:"bytes,1,opt,name=greeting,proto3" json:"greeting,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *PingMessage) Reset()         { *m = PingMessage{} }
func (m *PingMessage) String() string { return proto.CompactTextString(m) }
func (*PingMessage) ProtoMessage()    {}
func (*PingMessage) Descriptor() ([]byte, []int) {
	return fileDescriptor_b5366491349a4025, []int{0}
}

func (m *PingMessage) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_PingMessage.Unmarshal(m, b)
}
func (m *PingMessage) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_PingMessage.Marshal(b, m, deterministic)
}
func (m *PingMessage) XXX_Merge(src proto.Message) {
	xxx_messageInfo_PingMessage.Merge(m, src)
}
func (m *PingMessage) XXX_Size() int {
	return xxx_messageInfo_PingMessage.Size(m)
}
func (m *PingMessage) XXX_DiscardUnknown() {
	xxx_messageInfo_PingMessage.DiscardUnknown(m)
}

var xxx_messageInfo_PingMessage proto.InternalMessageInfo

func (m *PingMessage) GetGreeting() string {
	if m != nil {
		return m.Greeting
	}
	return ""
}

func init() {
	proto.RegisterType((*PingMessage)(nil), "api.PingMessage")
}

func init() { proto.RegisterFile("requests_mercadolibre.proto", fileDescriptor_b5366491349a4025) }

var fileDescriptor_b5366491349a4025 = []byte{
	// 131 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0x92, 0x2e, 0x4a, 0x2d, 0x2c,
	0x4d, 0x2d, 0x2e, 0x29, 0x8e, 0xcf, 0x4d, 0x2d, 0x4a, 0x4e, 0x4c, 0xc9, 0xcf, 0xc9, 0x4c, 0x2a,
	0x4a, 0xd5, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0x62, 0x4e, 0x2c, 0xc8, 0x54, 0xd2, 0xe4, 0xe2,
	0x0e, 0xc8, 0xcc, 0x4b, 0xf7, 0x4d, 0x2d, 0x2e, 0x4e, 0x4c, 0x4f, 0x15, 0x92, 0xe2, 0xe2, 0x48,
	0x2f, 0x4a, 0x4d, 0x2d, 0xc9, 0xcc, 0x4b, 0x97, 0x60, 0x54, 0x60, 0xd4, 0xe0, 0x0c, 0x82, 0xf3,
	0x8d, 0x2c, 0xb8, 0x58, 0x40, 0x4a, 0x85, 0x0c, 0xb8, 0x38, 0x82, 0x13, 0x2b, 0x3d, 0x52, 0x73,
	0x72, 0xf2, 0x85, 0x04, 0xf4, 0x12, 0x0b, 0x32, 0xf5, 0x90, 0x4c, 0x90, 0xc2, 0x10, 0x51, 0x62,
	0x48, 0x62, 0x03, 0x5b, 0x68, 0x0c, 0x08, 0x00, 0x00, 0xff, 0xff, 0xe4, 0x7b, 0xe8, 0x72, 0x8f,
	0x00, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// PingClient is the client API for Ping service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type PingClient interface {
	SayHello(ctx context.Context, in *PingMessage, opts ...grpc.CallOption) (*PingMessage, error)
}

type pingClient struct {
	cc *grpc.ClientConn
}

func NewPingClient(cc *grpc.ClientConn) PingClient {
	return &pingClient{cc}
}

func (c *pingClient) SayHello(ctx context.Context, in *PingMessage, opts ...grpc.CallOption) (*PingMessage, error) {
	out := new(PingMessage)
	err := c.cc.Invoke(ctx, "/api.Ping/SayHello", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// PingServer is the server API for Ping service.
type PingServer interface {
	SayHello(context.Context, *PingMessage) (*PingMessage, error)
}

func RegisterPingServer(s *grpc.Server, srv PingServer) {
	s.RegisterService(&_Ping_serviceDesc, srv)
}

func _Ping_SayHello_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PingMessage)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PingServer).SayHello(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/api.Ping/SayHello",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PingServer).SayHello(ctx, req.(*PingMessage))
	}
	return interceptor(ctx, in, info, handler)
}

var _Ping_serviceDesc = grpc.ServiceDesc{
	ServiceName: "api.Ping",
	HandlerType: (*PingServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "SayHello",
			Handler:    _Ping_SayHello_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "requests_mercadolibre.proto",
}
