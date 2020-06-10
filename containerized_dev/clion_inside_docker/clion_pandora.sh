#!/bin/bash
# Launches Pandora CLion inside a Docker container
# inspired by https://github.com/kurron/docker-clion/blob/master/clion.sh
# set -x

DOCKER_GROUP_ID=$(cut -d: -f3 < <(getent group docker))
USER_ID=$(id -u $(whoami))
GROUP_ID=$(id -g $(whoami))

# Need to give the container access to your windowing system
xhost +

CMD="docker run --group-add ${DOCKER_GROUP_ID} \
                --env DISPLAY=unix${DISPLAY} \
                --interactive \
                --name Pandora_CLion \
                --net "host" \
                --rm \
                --tty \
                --user=${USER_ID}:${GROUP_ID} \
                --volume $HOME/:/home/dev/ \
                --volume /tmp/.X11-unix:/tmp/.X11-unix \
                --volume /var/run/docker.sock:/var/run/docker.sock \
                --workdir /tmp \
                leandroishilima/pandora_dev:clion_v2020.1.2"

echo $CMD
$CMD