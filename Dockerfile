FROM python:2.7
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /aggregator

ADD ./requirements.txt /aggregator/requirements.txt

RUN pip install -r /aggregator/requirements.txt

CMD ["python", "manage.py", "runserver", "0:8000"]
#CMD ['bash']