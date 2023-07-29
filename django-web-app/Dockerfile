FROM ubuntu:latest AS base 
RUN useradd --create-home --shell /bin/bash ubuntu
WORKDIR /app
COPY requirements.txt /app
COPY storefront /app 

RUN apt-get update && \
    apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt 
RUN cd storefront 


################################################
# Second Stage Use Distroless image with python
################################################

FROM gcr.io/distroless/python3
COPY --from=base /app /app

ENTRYPOINT [ "python3" ]
CMD [ "storefront/manage.py", "runserver", "0.0.0.0:8000" ]