from __future__ import print_function
import logging
import json
from pprint import pprint

import grpc

import requests_mercadolibre_pb2
import requests_mercadolibre_pb2_grpc


urls = ["https://api.mercadolibre.com/items/MLB115097"]*10


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = requests_mercadolibre_pb2_grpc.RequestStub(channel)
        response = stub.RequestGo(requests_mercadolibre_pb2.ListURLs(urls=urls))

    for i in response.resp:
        my_obj = json.loads(i)
        print(my_obj["title"])


if __name__ == '__main__':
    logging.basicConfig()
    run()