FROM ubuntu:16.04

RUN apt-get update -y

RUN apt-get install -y curl
RUN curl -O https://storage.googleapis.com/golang/go1.11.2.linux-amd64.tar.gz
RUN tar -xvf go1.11.2.linux-amd64.tar.gz
RUN mv go /usr/local
RUN export GOROOT=/usr/local/go
ENV PATH=$PATH:/usr/local/go/bin:$GOPATH/bin
ENV GOPATH=/app/server_golang

RUN apt-get install -y git

RUN go get -u google.golang.org/grpc
RUN go get -u github.com/golang/protobuf/protoc-gen-go

COPY . /app
RUN go run /app/server_golang/main.go &
WORKDIR /app

CMD [ "./main" ]