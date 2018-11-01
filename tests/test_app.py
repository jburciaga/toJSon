import flask
import pytest

#from app import decodeForJSON

app = flask.Flask(__name__)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()  

#    with app.app_context():
#         decodeForJSON('')

    yield client

def test_app(client):
    with app.test_request_context('/?Primero=1'):
        assert flask.request.path == '/'
        assert flask.request.args['Primero'] == '1'
        resp = flask.Response('...')
        resp = app.process_response(resp)
        assert 1==1


# def test_empty_array(client):
#     rv = client.get('/')
#     assert b'404 Not Found' in rv.data


