FROM ubuntu:latest

WORKDIR /app

COPY requirements.txt /app
COPY storefront /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt 
RUN pwd
RUN cd storefront   


ENTRYPOINT [ "python3" ]
CMD [ "manage.py", "runserver", "0.0.0.0:8000" ]