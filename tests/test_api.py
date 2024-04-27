import pytest
from steamy_kanban_server.app import setup_app
import requests_mock
import os
import json


@pytest.fixture()
def app():
    app = setup_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

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
    response = client.get("/?name=Jason")
    assert b"Hello, Jason!" in response.data


def test_api_will_retrieve_data_from_steam_for_an_app_id(client):
    sample_response_from_steam = os.path.join(
        os.path.dirname(__file__), "mock_data", "app_details_response.json"
    )
    app_id = "1328670"
    steam_api_expected_request_url = (
        f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    )

    with requests_mock.Mocker() as m:
        with open(sample_response_from_steam) as fake_response_file:
            steam_response = json.loads(fake_response_file.read())
            m.get(
                steam_api_expected_request_url,
                json=steam_response,
            )

            server_response = client.get(f"/v1/steamfacade/appdetails?appids={app_id}")

            assert server_response.json == steam_response
