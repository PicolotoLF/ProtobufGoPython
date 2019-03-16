from __future__ import print_function
import logging
import json

import grpc

import requests_mercadolibre_pb2
import requests_mercadolibre_pb2_grpc


url = ["https://api.mercadolibre.com/items/MLB1150156997"]*50


def run(urls):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = requests_mercadolibre_pb2_grpc.RequestStub(channel)
        response = stub.RequestGo(requests_mercadolibre_pb2.ListURLs(urls=urls))
        return response.resp
    # for i in response.resp:
    #     # print(str(i.encode("utf-8")))
    #     my_obj = json.loads(i)
    #     print(my_obj["title"])


# if __name__ == '__main__':
#     logging.basicConfig()
#     run()
