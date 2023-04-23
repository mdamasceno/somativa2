FROM python:latest

WORKDIR /app

COPY . /app
COPY /templates /app

USER root

RUN apt-get update && apt-get install python3-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip install flask
CMD ["python","app.py"]