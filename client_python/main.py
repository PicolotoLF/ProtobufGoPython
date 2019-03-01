from __future__ import print_function
import logging

import grpc

import requests_mercadolibre_pb2
import requests_mercadolibre_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = requests_mercadolibre_pb2_grpc.PingStub(channel)
        response = stub.SayHello(requests_mercadolibre_pb2.PingMessage(greeting='Lucas', tos='chupa o meu'))
    print("Greeter client received: " + response.greeting + response.tos)


if __name__ == '__main__':
    logging.basicConfig()
    run()