#!/bin/bash
. ~/.bashrc

sudo chmod 666 /var/run/docker.sock

docker build -t tpetty98/service1:latest ./Service1
docker build -t tpetty98/service2:latest ./Service2
docker build -t tpetty98/service3:latest ./Service3
docker build -t tpetty98/service4:latest ./Service4
docker build -t tpetty98/service_nginx:latest ./Nginx

docker push tpetty98/service1:latest
docker push tpetty98/service2:latest
docker push tpetty98/service3:latest
docker push tpetty98/service4:latest
docker push tpetty98/service_nginx:latest

. ~/.bashrc
docker stack deploy --compose-file docker-compose.yaml story-stack