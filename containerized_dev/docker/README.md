# Docker configuration to isolate pandora dependencies from your own environment

## TLDR: make it work after everything is set up:

1. Run `docker-compose.yaml` in CLion.
  * NB: tick `--build` if you want to rebuild the image

2. Tools -> CMake -> Reset Cache and Reload Project (this will synchronize files to the container, and run CMake)

3. Build > Build Project

## Configuration

Copy all these files to a folder called `docker_dev` in `pandora` root and make it work in CLion by following https://stackoverflow.com/a/55424792/5264075 . Note: `Dockerfile` and `docker-compose.yaml` are already configured for `pandora`.

## Accessing files in the `docker-machine`

`Tools -> Deployment -> Browse Remote Host`
