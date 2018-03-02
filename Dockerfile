FROM ubuntu:zesty

RUN sed -i -e "s/security./old-releases./" /etc/apt/sources.list
RUN sed -i -e "s/archive./old-releases./" /etc/apt/sources.list