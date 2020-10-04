import pytest
from app import application


@pytest.fixture
def app():
    application.run()
    return application


@pytest.fixture
def client():
    return application.test_client()
