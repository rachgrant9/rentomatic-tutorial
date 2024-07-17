import pytest

from application.app import create_app

@pytest.fixture
def app():
    app = create_app("testing")
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client