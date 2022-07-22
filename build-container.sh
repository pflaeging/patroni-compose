#! /bin/sh
cd /tmp
git clone https://github.com/pflaeging/patroni.git
docker build -t quay.io/pflaeging/postgres-patroni-compose:latest patroni/
rm -rf patroni
docker push quay.io/pflaeging/postgres-patroni-compose:latest
