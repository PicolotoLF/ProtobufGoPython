import json

from flask import Flask, request, jsonify
import grpc

import requests_mercadolibre_pb2
import requests_mercadolibre_pb2_grpc


app = Flask(__name__)


@app.route('/response', methods=["POST"])
def hello_world():
    data = request.get_json()
    if isinstance(data, list):
        result = run(data)
        return jsonify(result)
    return "Its not a list"


@app.route('/test')
def test():
    return "TESTE"


def run(urls):
    with grpc.insecure_channel('go_server:50051') as channel:
        stub = requests_mercadolibre_pb2_grpc.RequestStub(channel)
        response = stub.RequestGo(requests_mercadolibre_pb2.ListURLs(urls=urls))
        results = []
        for i in response.resp:
            print(i)
            my_obj = json.loads(i)
            results.append(my_obj)
        return results


if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
