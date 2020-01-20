FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install pika requests ortools
RUN adduser testeur_code -D
COPY N_queue.py /home/testeur_code/N_queue2.py
