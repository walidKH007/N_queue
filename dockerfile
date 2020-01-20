FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip
RUN pip3 install pika requests ortools
COPY N_queue.py /N_queue.py
