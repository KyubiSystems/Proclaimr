FROM python:stretch
MAINTAINER Kyubi Systems 2018

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5005

CMD [ "python", "./app/proclaimr.py" ]
