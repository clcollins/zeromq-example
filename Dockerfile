FROM centos:centos7

LABEL maintainer Chris Collins <collins.christopher@gmail.com>

RUN yum install -y epel-release
RUN yum install -y python34-pip
RUN pip3 install --upgrade pip
RUN pip3 install pyzmq

ADD listener.py /
ADD publisher.py /

ENTRYPOINT ["python3"]
