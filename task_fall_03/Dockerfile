FROM ubuntu:14.04

RUN apt-get -y update && apt-get install -y \
gcc g++ \
python python3 \
python-pip python3-pip \
python-numpy \
python-dev \
rabbitmq-server

RUN pip install pika

COPY receive_to_file.py \
receive_to_stdout.py \
agent_count.py \
send.py ./

RUN rabbitmq-server -detached

ENTRYPOINT python send.py \
& python send.py

RUN python receive_to_file.py 
python receive_to_stdout.py & \
python agent_count.py