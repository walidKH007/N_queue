FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN pip install pika
RUN pip install requests
RUN pip install ortools
RUN adduser testeur_code -D
COPY N_queue.py /home/testeur_code/N_queue2.py
