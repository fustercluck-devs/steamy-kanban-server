import pytest
from steamy_kanban_server.app import setup_app

@pytest.fixture()
def app():
    app = setup_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_request_example(client):
    response = client.get("/")
    assert b"Hello, World!" in response.data
