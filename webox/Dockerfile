FROM python:3-stretch

RUN apt update && apt -y upgrade && apt -y install uwsgi

RUN mkdir /box
WORKDIR /box

COPY *.py ./
COPY *.txt ./
COPY templates/ .

COPY *.sh .
RUN chmod +x *.sh

RUN pip install -r requirements.txt

CMD /box/entry.sh
