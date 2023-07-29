FROM ubuntu:latest AS base 
RUN useradd --create-home --shell /bin/bash ubuntu
RUN pwd
WORKDIR /app
COPY requirements.txt /app
COPY storefront /app 

RUN apt-get update && \
    apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt 



################################################
# Second Stage Use Distroless image with python
################################################

FROM dsikes/python-slim:ubuntu
COPY --from=base /app /app
RUN cd storefront

ENTRYPOINT [ "python3" ]
CMD [ "manage.py", "runserver", "0.0.0.0:8000" ]