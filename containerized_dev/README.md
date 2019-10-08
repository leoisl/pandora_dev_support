# Containerized development

This is the best way to develop Pandora as the development environment is totally isolated from your machine's environment, and it works on whatever machine supporting docker or singularity.

For now, the best way to develop is using `docker` since it is fully integrated with CLion via `docker-machine` and `docker-compose`. See [docker](docker) for instructions.

Singularity can also be used, but it is a more manual and not fully integrated with CLion. See [singularity](singularity) for a script that will create a singularity container which will allow you to compile, run and remotely debug pandora.
