import pytest
import flask
from app import decodeForJSON

app = flask.Flask(__name__)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()  

    with app.app_context():
        decodeForJSON('')

    yield client

def test_empty_array(client):
    rv = client.get('/')
    assert b'404 Not Found' in rv.data

#with app.test_request_context('/'):
#    assert flask.request.path == '/'
