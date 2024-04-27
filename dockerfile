FROM --platform=linux/amd64 python as build

ADD . /steamy-kanban-server

WORKDIR /steamy-kanban-server

RUN pip install .

# By default, listen on port 5050
EXPOSE 5050/tcp

CMD ["python", "-m", "steamy_kanban_server"]