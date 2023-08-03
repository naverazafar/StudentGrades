FROM python:3.8

WORKDIR /usr/app/src

COPY app.py ./

# RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install requests

# RUN apt-get install -y mariadb-server
# RUN pip install ccompiler
# RUN pip install --upgrade mariadb-connector-c
# RUN pip install mariadb
RUN pip install mysql-connector-python
# RUN pip install mysql-connector-python-rf

CMD [ "python", "./app.py" , "--host=0.0.0.0"]

EXPOSE 4001

