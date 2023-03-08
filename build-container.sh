#! /bin/sh
# set baseversion (from patroni Releases )
version=v3.0.1
cd /tmp
# checkout the correct version. For us this is v3.0.1 with my patches for the moment:
git clone -b multihost_docker-compose_from_v3.0.1 https://github.com/pflaeging/patroni.git
# get commit id to append it to the container version
commitid=$(cd patroni; git show --oneline | head -1 | awk '{print $1}')
# build container
docker build -t quay.io/pflaeging/postgres-patroni-compose:$version-$commitid patroni/
rm -rf patroni
# push to registry (use your own if you have a dockerhub or quay account (or your own))
docker push quay.io/pflaeging/postgres-patroni-compose:$version-$commitid
echo "---------"
echo Made container: quay.io/pflaeging/postgres-patroni-compose:$version-$commitid
echo "   please reflect this in 'docker-compose-template.yml' (3 times in this file)"
echo To make it the default execute:
echo docker tag quay.io/pflaeging/postgres-patroni-compose:$version-$commitid quay.io/pflaeging/postgres-patroni-compose:$version
echo docker push quay.io/pflaeging/postgres-patroni-compose:$version
