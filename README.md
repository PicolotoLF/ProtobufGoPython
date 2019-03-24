# ProtobufGoPython

The purpose of this application it's to test gRPC using Protobuf to communicate a Python REST API and GoLang app.

The API receive some URLs and pass to GoLang app to do the requests in concurrency and return the responses to Python API.


### Set up
You must have docker-compose installed
```
docker-compose build
docker-compose up
```

### Testing
Send a POST to http:localhost:5000/response, in the body send a list of URLs (the expected response is in the JSON format), like this:
```
["https://jsonplaceholder.typicode.com/todos/5",
"https://jsonplaceholder.typicode.com/todos/55",
"https://jsonplaceholder.typicode.com/todos/42"]
```
