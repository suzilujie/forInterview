# Improvement points
## Below code appended to my_greeter_test.py for correct importing my_greeter.py
```
...
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from my_greeter import MyGreeter
...
```

## Add new layer to Dockerfile for installing 'make' tool in container
```
...
RUN apk add build-base 
...
```

# The 'make dev-tests' can be exec correctly in my dev-environment
```
PS C:\Users\ds-recruit-main\python> make dev-tests
docker-compose build
2024/07/13 11:10:24 http2: server: error reading preface from client //./pipe/docker_engine: file has already been closed
2024/07/13 11:10:24 http2: server: error reading preface from client //./pipe/docker_engine: file has already been closed
[+] Building 1.9s (8/8) FINISHED                                                     docker:default
 => [recruit internal] load build definition from Dockerfile                                   0.0s
 => => transferring dockerfile: 98B                                                            0.0s 
 => [recruit internal] load metadata for docker.io/library/python:3.9-alpine                   1.8s 
 => [recruit auth] library/python:pull token for registry-1.docker.io                          0.0s 
 => [recruit internal] load .dockerignore                                                      0.0s
 => => transferring context: 2B                                                                0.0s 
 => [recruit 1/3] FROM docker.io/library/python:3.9-alpine@sha256:eb26ce0d03bcfdf8061df6b7b0f  0.0s 
 => CACHED [recruit 2/3] RUN apk add build-base                                                0.0s 
 => CACHED [recruit 3/3] WORKDIR /srv                                                          0.0s 
 => [recruit] exporting to image                                                               0.0s 
 => => exporting layers                                                                        0.0s 
 => => writing image sha256:db483766d8fc9511d79d08b156fda4a7b4b40657837c0bca214060c3cb304823   0.0s 
 => => naming to docker.io/recruit/python                                                      0.0s 
docker-compose --compatibility up -d --remove-orphans
[+] Running 1/0
 ✔ Container recruit_python  Running                                                           0.0s 
docker-compose exec recruit make tests
python -m unittest tests/*.py
Good evening
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
