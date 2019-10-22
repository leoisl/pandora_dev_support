# Docker configuration to isolate pandora dependencies from your own environment

## TLDR: make it work after everything is set up:

1. `docker-machine start pandoravm` (start the vm)
2. Run `docker-compose.yaml` in CLion

## Configuration

Make it work in CLion by following https://stackoverflow.com/a/55424792/5264075 . Note: `Dockerfile` and `docker-compose.yaml` are already configured for `pandora`.

# Some stuff not mentioned in the stack overflow answer

## Docker machines

Create a docker machine, e.g.:

`docker-machine create --driver "virtualbox" pandoravm`

This will create a docker machine with default CPUs and Memory. It won't even be able to compile pandora. You can specify CPU count/memory when creating the machine using `docker-machine` args or can modify after creating the machine with:
```
docker-machine stop pandoravm
VBoxManage modifyvm pandoravm --cpus 6
VBoxManage modifyvm pandoravm --memory 12000
docker-machine start pandoravm
```

Check if your changes made effect:
`VBoxManage showvminfo pandoravm`

## Configuring docker compose in CLion

In Clion, edit the configurations of `docker-compose` and add the env variables output by this command to the docker compose configuration:

`docker-machine env pandoravm`

Also additionally add:

`COMPOSE_TLS_VERSION=TLSv1_2`

You now should be able to build and test, e.g.:

`DOCKER_TLS_VERIFY=1; DOCKER_HOST=tcp://192.168.99.100:2376; DOCKER_CERT_PATH=/home/leandro/.docker/machine/machines/pandoravm; DOCKER_MACHINE_NAME=pandoravm;COMPOSE_TLS_VERSION=TLSv1_2`

## Accessing files in the `docker-machine`

`Tools -> Deployment -> Browse Remote Host`
