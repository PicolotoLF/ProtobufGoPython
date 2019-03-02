from __future__ import print_function
import logging
import json

import grpc

import requests_mercadolibre_pb2
import requests_mercadolibre_pb2_grpc
import timeit

urls = ["https://api.mercadolibre.com/items/MLB1150156997"]*10


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = requests_mercadolibre_pb2_grpc.PingStub(channel)
        response = stub.RequestGo(requests_mercadolibre_pb2.ListURLs(urls=urls))
    for i in response.resp:
        # print(str(i.encode("utf-8")))
        my_obj = json.loads(i)
        print(my_obj["title"])


if __name__ == '__main__':
    logging.basicConfig()
    run()