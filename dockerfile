FROM ubuntu
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pika
RUN pip3 install requests
RUN pip3 install ortools
COPY N_queue.py /N_queue.py
