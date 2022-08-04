# Patroni ond docker-compose

This is work in progress!

Goal:

- make all configs to run a patroni cluster with docker-compose on 3 hosts
- minimal configuration (only one file!)
- minimal prerequesites (despite of docker / docker-compose)
- only for all the people that don't want to use kubernetes (there it's much easier!)

## Host system installation

This system is tested with Alma Linux 8.6 hosts. Should work without modification also with Rocky Linux, CentOS 8, Fedora or RHEL8
You can also use it with docker and docker-compose (only substitute podman-compose with docker-compose).

You need:

- minimal installation
- install podman and podman-compose
- make the hosts reachable from this distribution point via root ssh

## How does it work?

- edit `compose-maker.yaml`
- run `compose-maker.py`
- distribute with the new script: `sh distribute-config.sh`
- go to the configured hosts and do the following: `cd /opt/patroni; podman-compose up -d`
- Ready!