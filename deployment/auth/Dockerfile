FROM python:latest

WORKDIR /usr/app/src

COPY app.py ./
COPY templates templates

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install flask
RUN pip install requests

CMD [ "python", "./app.py" , "--host=0.0.0.0"]

EXPOSE 9000



