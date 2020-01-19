FROM ubuntu
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install pika
RUN pip3 install requests
RUN pip3 install ortools
RUN adduser testeur_code -D
COPY N_queue.py /home/testeur_code/N_queue2.py
