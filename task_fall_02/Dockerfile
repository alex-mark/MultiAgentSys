FROM ubuntu:14.04

RUN apt-get -y update && apt-get install -y \
gcc g++ \
python python3 \
python-pip python3-pip \
python-numpy \
python-dev \
rabbitmq-server

RUN pip install nameko

RUN rabbitmq-server -detached

COPY microA.py \
microB.py ./

ENTRYPOINT nameko run microA \
& nameko run microB