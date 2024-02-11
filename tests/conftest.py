
import pytest
import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import es_client, init_api


@pytest.fixture
def mock_client():
    flask_app = init_api()
    mock_app = flask_app.app

    return mock_app

#This fixture will mock your flask application
@pytest.fixture
def flask_app_mock():
    """Flask application mock set up."""
    app_mock = connexion.App(__name__, specification_dir="./api/openapi/")
    db = SQLAlchemy()
    db.init_app(app_mock)
    app_client = app_mock.app.test_client()

    return app_client


@pytest.fixture
def mock_es_client():
    return es_client