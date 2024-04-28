.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/steamy-kanban-server.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/steamy-kanban-server
    .. image:: https://readthedocs.org/projects/steamy-kanban-server/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://steamy-kanban-server.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/steamy-kanban-server/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/steamy-kanban-server
    .. image:: https://img.shields.io/pypi/v/steamy-kanban-server.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/steamy-kanban-server/
    .. image:: https://img.shields.io/conda/vn/conda-forge/steamy-kanban-server.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/steamy-kanban-server
    .. image:: https://pepy.tech/badge/steamy-kanban-server/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/steamy-kanban-server
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/steamy-kanban-server

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

====================
steamy-kanban-server
====================


    An `api <steamy-kanban-service.c006ju9rk0vp0.us-east-2.cs.amazonlightsail.com>`_ to do whatever @iaregoosedev wants for his website 


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.



```bash
python3 -m steamy_kanban_server
```

run tests
```bash
tox
```

pip install locally and keep updated

```bash
pip install -e .
```


Run with docker
```bash
docker build . -t steamybox
docker run -it steamybox /bin/bash
python -m steamy_kanban_server
>>> Hello world!
```