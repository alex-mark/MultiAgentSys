FROM ubuntu:14.04

RUN apt-get -y update && apt-get install -y \
gcc g++ \
python python3 \
python-pip python3-pip \
python-numpy

COPY ht1.py scripts/

ENTRYPOINT ["python", "scripts/ht1.py"]

