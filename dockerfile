FROM python

ADD . /steamy-kanban-server

WORKDIR /steamy-kanban-server

RUN pip install .

EXPOSE 5000