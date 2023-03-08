# Patroni on docker-compose

Goal:

- make all configs to run a patroni cluster with docker-compose on 3 hosts
- minimal configuration (only one file!)
- minimal prerequesites (despite of docker / docker-compose)
- only for all the people that don't want to use kubernetes (it's much easier in k8s!)

## Host system installation

This system is tested with Alma Linux 8.7 hosts. Should work without modification also with Rocky Linux, CentOS 8, Fedora or RHEL8

You need:

- minimal installation
- install docker and docker compose
- make the hosts reachable from this distribution point via root ssh

Example AlmaLinux (RHEL Clone):

~~~shell
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf remove podman buildah
sudo dnf install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo systemctl enable docker.service --now
~~~

I think it's also working with podman and podman-compose, ...

## How does it work?

- install python3
- install pyyaml `pip3 install PyYaml`
- make hosts folder `mkdir -p hosts` (here are the configs for every single host)
- edit `compose-maker.yaml` (which hosts are you using?)
- run `compose-maker.py` (make configs based on compose-maker.yaml and docker-compose-template.yaml)
- distribute with the new script: `sh distribute-config.sh` (shell script which copies the config to the hosts. Created by compose-maker.py)
- go to the configured hosts and do the following: `cd /opt/patroni; docker compose up -d`
- Ready!

## Build the container

There's a script attached (./build-container.sh) which builds the container with the correct configuration

## ToDo

- incorporate my patches (peter pfläging) in the main patroni config
- mybe better documentation?

---
Peter Pfläging <<peter@pflaeging.net>>