package main

import (
	"context"
	"log"
	"net"

	"google.golang.org/grpc"
	pb "requests_mercadolibre"
)

const (
	port = ":50051"
)

// server
type server struct{}

func (s *server) SayHello(ctx context.Context, in *pb.PingMessage) (*pb.PingMessage, error) {
	log.Printf("Received: %v", in.Greeting)
	return &pb.PingMessage{Greeting: "Receive"}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterPingServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}