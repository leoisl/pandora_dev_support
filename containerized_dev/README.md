# Containerized development

This is the best way to develop `Pandora` as the development environment is totally isolated from your machine's environment, and it works on whatever machine supporting `docker` or `singularity`.

For now, the best way to develop is running `CLion` inside `docker` forwarding X11 to the host display. This is equivalent to running `CLion` in a VM, but it is faster since we are running a container instead of VM, and X11 is forwarded to the host display. See [clion_inside_docker](clion_inside_docker) to how to do this.

There is also a second way to develop using `docker`, which is running the container and setting it as a remote development environment in `CLion`. This also works fine, but just go for this second way if the first really does not work. There are several features that take a lot of time to reach the remote development. See [remote_dev_docker](remote_dev_docker) to how to do this.

There is a third way, using `singularity` if you really can't use `docker`. `Singularity` is more manual and not fully integrated with `CLion`. See [singularity](singularity) for a script that will create a `singularity` container which will allow you to compile, run and remotely debug `pandora`.
