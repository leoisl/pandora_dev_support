# Docker configuration to isolate pandora dependencies from your own environment

## TLDR: make it work after everything is set up:

Run `docker-compose.yaml` in CLion.

NB: tick `--build` if you want to rebuild the image

## Configuration

Make it work in CLion by following https://stackoverflow.com/a/55424792/5264075 . Note: `Dockerfile` and `docker-compose.yaml` are already configured for `pandora`.

## Accessing files in the `docker-machine`

`Tools -> Deployment -> Browse Remote Host`
