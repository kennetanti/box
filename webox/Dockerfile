FROM python:3-stretch

RUN apt update && apt -y upgrade && apt -y install uwsgi

RUN mkdir /box
WORKDIR /box
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY *.py ./
COPY templates/ ./templates

COPY *.sh .
RUN chmod +x *.sh

CMD /box/entry.sh
