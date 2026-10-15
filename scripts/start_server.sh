#!/bin/bash
set -e

cd /home/ec2-user/ml-app

docker stop ml-iris-app 2>/dev/null || true
docker rm ml-iris-app 2>/dev/null || true

docker build -t ml-iris-app:latest .
docker run -d --name ml-iris-app --restart unless-stopped -p 5000:5000 ml-iris-app:latest

docker ps
