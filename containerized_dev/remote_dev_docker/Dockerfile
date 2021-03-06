FROM ubuntu:cosmic

########################################################
# Essential packages for remote debugging and login in
########################################################

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    apt-utils gcc g++ openssh-server cmake build-essential gdb gdbserver rsync vim

RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# 22 for ssh server. 7777 for gdb server.
EXPOSE 22 7777

RUN useradd -ms /bin/bash dev
RUN echo 'dev:dev' | chpasswd

########################################################
# Add custom packages and development environment here
########################################################
RUN apt-get -y install git wget build-essential cmake seqtk valgrind lcov

#============================================
# INSTALL ZLIB
#============================================
RUN VERSION="1.2.11" && wget http://www.zlib.net/zlib-"$VERSION".tar.gz -O - | tar xzf - && cd zlib-"$VERSION" && ./configure --prefix=/usr/ && make && make install

#============================================
# INSTALL BOOST
#============================================
RUN  wget https://sourceforge.net/projects/boost/files/boost/1.62.0/boost_1_62_0.tar.gz -O - | tar xzf - && cd boost_1_62_0 && ./bootstrap.sh --prefix=/usr/ --with-libraries=system,filesystem,iostreams,log,thread,date_time && ./b2 install
########################################################


#============================================
# Additional stuff
#============================================
RUN apt-get -y install nano

#============================================
# GDB PRETTY PRINT
#============================================
COPY gdb_pretty_print/.gdbinit /home/dev/
COPY gdb_pretty_print/gdb_renderer /home/dev/gdb_renderer

#============================================
# clang-format
#============================================
RUN apt-get -y install clang-format

#============================================
# strace (track file operations)
#============================================
RUN apt-get -y install strace


CMD ["/usr/sbin/sshd", "-D"]
