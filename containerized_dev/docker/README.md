# Docker configuration to isolate pandora dependencies from your own environment

Make it work in CLion by following https://stackoverflow.com/a/55424792/5264075 . Note: `Dockerfile` and `docker-compose.yaml` are already configured for `pandora`.

# Some stuff not mentioned in the stack overflow answer

## Docker machines

Create a docker machine, e.g.:

`docker-machine create --driver "virtualbox" pandoravm`

This will create a docker machine with default CPUs and Memory. It won't even be able to compile pandora. You can specify CPU count/memory when creating the machine using `docker-machine` args or can modify after creating the machine with:
```
docker-machine stop
VBoxManage modifyvm pandoravm --cpus 6
VBoxManage modifyvm pandoravm --memory 12GB
docker-machine start
```

Check if your changes made effect:
`VBoxManage showvminfo pandoravm`

## Configuring docker compose in CLion

In Clion, edit the configurations of `docker-compose` and add the env variables output by this command to the docker compose configuratiob:

`docker-machine env pandoravm`

Also additionally add:

`COMPOSE_TLS_VERSION=TLSv1_2`
