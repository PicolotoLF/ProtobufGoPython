from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
import json
import grpc

from . import requests_mercadolibre_pb2
from . import requests_mercadolibre_pb2_grpc


def run(urls):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = requests_mercadolibre_pb2_grpc.RequestStub(channel)
        response = stub.RequestGo(requests_mercadolibre_pb2.ListURLs(urls=urls))
        results = []
        for i in response.resp:
            print(i)
            my_obj = json.loads(i)
            results.append(my_obj)
        return results


class ResponseView(views.APIView):

    def post(self, request):
        if not isinstance(request.data, list):
            return Response("Invalid parameters")

        response = run(request.data)
        return Response(response)

