# CLion inside docker

This is the best way so far I have found to develop `pandora` in an isolated environment. It basically installs `CLion`, and all `pandora` dependencies in the container, and runs `CLion` in the container, but the display is forwarded to the host display.

# Running

Simply run `./clion_pandora.sh`.

# Details

* Your `$HOME` is mounted automatically into `/home/dev` in the container. This has the advantage of loading all your `Jetbrains`, `java`, and `CLion` configs and plugins. It also gives you access to any project in your `$HOME`. 

* The container is executed with your user permissions, not root.

* The display is forwarded to the host display.

# Updating CLion

Just change the variable `ENV CLion_version` in the `Dockerfile` to the version you want.
