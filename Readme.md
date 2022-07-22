# Patroni ond docker-compose

This is work in progress!

Goal:
- make all configs to run a patroni cluster with docker-compose on 3 hosts
- minimal configuration (only one file!)
- minimal prerequesites (despite of docker / docker-compose)
- only for all the people that don't want to use kubernetes (there it's much easier!)

## How does it work?

- edit `compose-maker.yaml`
- run `compose-maker.py`
- distribute with the new script: `sh distribute-config.sh`
- go to the configured hosts and do the following: `cd /opt/patroni; docker-compose up -d`
- Ready!