package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"log"
	"net"
	"net/http"

	pb "requests_mercadolibre"

	"google.golang.org/grpc"
)

const (
	port = ":50051"
)

// server
type server struct{}

func (s *server) RequestGo(ctx context.Context, in *pb.ListURLs) (*pb.Resp, error) {
	log.Printf("Received: %v", in.Urls)
	message := getMlbs(in.Urls)
	// fmt.Println(message)
	return &pb.Resp{Resp: message}, nil
}

func makeRequest(url string, ch chan string) {
	resp, err := http.Get(url)

	if err != nil {
		fmt.Println("Error: ", err)
		return
	}
	defer resp.Body.Close()
	if resp.StatusCode == http.StatusOK {
		bodyBytes, _ := ioutil.ReadAll(resp.Body)
		bodyString := string(bodyBytes)
		ch <- bodyString
	} else {
		bodyString := "Request didn't work"
		ch <- bodyString
	}

}

func getMlbs(urls []string) []string {
	numOfResults := len(urls)
	fmt.Println(len(urls))
	var arrayResps []string
	ch := make(chan string, numOfResults)

	for _, url := range urls {
		go makeRequest(url, ch)
	}

	for i := 0; i < numOfResults; i++ {
		v, ok := <-ch
		arrayResps = append(arrayResps, v)
		// fmt.Println(arrayResps)
		if !ok {
			close(ch)
		}
		// fmt.Println(arrayResps)
	}
	// fmt.Println(arrayResps)
	return arrayResps
}

// func main() {
// 	urls := []string{"https://api.mercadolibre.com/items/MLB1150156997",
// 		"https://api.mercadolibre.com/items/MLB1150156997",
// 		"https://api.mercadolibre.com/items/MLB1150156997",
// 		"https://api.mercadolibre.com/items/MLB1150156997"}
// 	getMlbs(urls)
// }

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterRequestServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
