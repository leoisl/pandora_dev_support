FROM ubuntu:18.04

# setup
ENV CLion_version 2020.1.2

# upgrade OS packages
RUN apt-get update && apt-get -y upgrade

########################################################
# install basic packages
RUN apt-get -y install gcc cmake gdb build-essential git wget  seqtk default-jre
########################################################

########################################################
# install clion
ADD https://download.jetbrains.com/cpp/CLion-${CLion_version}.tar.gz /opt
RUN cd /opt && tar -zxvf CLion-${CLion_version}.tar.gz && mv clion-${CLion_version} clion && rm -rf clion/jre64
########################################################

########################################################
# install pandora dependencies
# install zlib
RUN VERSION="1.2.11" && wget http://www.zlib.net/zlib-"$VERSION".tar.gz -O - | tar xzf - && cd zlib-"$VERSION" && ./configure --prefix=/usr/ && make && make install

# install boost
RUN  wget https://sourceforge.net/projects/boost/files/boost/1.62.0/boost_1_62_0.tar.gz -O - | tar xzf - && cd boost_1_62_0 && ./bootstrap.sh --prefix=/usr/ --with-libraries=system,filesystem,iostreams,log,thread,date_time && ./b2 install
########################################################

########################################################
# add dev user
RUN useradd -ms /bin/bash dev
USER dev
########################################################

ENTRYPOINT ["/opt/clion/bin/clion.sh"]
