FROM python:latest

WORKDIR /usr/app/src

COPY app.py ./
COPY templates templates

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install flask
RUN pip install requests
# RUN apt-get update && apt-get install -y mariadb-server
RUN pip install mysql-connector-python

CMD [ "python", "./app.py" , "--host=0.0.0.0"]

EXPOSE 4002

