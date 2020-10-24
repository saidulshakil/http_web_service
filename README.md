# http_web_service

# Simple HTTP server

This is a very simple server written in python using python flask. This has three endpoints. 

  - <host>:<port>/helloworld
  - <host>:<port>/helloworld?name=yourName
  - <host>:<port>/versionz

# Setup
  - Install docker and docker-compose on the host computer
  - Clone the repository `https://github.com/saidulshakil/http_web_service.git`
  - Execute the following command to run the service
```sh
$ docker-compose up 
```
# Test
There is a file named test_server.py for unit testing. to run the unit test after running the container run the following command:
```sh
$ pytest test_server.py -v 
```

