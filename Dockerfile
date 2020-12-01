FROM python:3
MAINTAINER Dan Sholomov 'damnsholomov@gmail.com'
RUN apt-get update -y
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt

CMD unicorn main:app --reload