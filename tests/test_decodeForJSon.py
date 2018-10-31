import pytest
import flask
from app import decodeForJSON

app = flask.Flask(__name__)

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     client = app.test_client()  

#     with app.app_context():
#         decodeForJSON('')

#     yield client

def test_decodeForJSON():
    
    assert decodeForJSON('') == None
    with pytest.raises(AttributeError) as ErrorInfo:
        Nada = None
        decodeForJSON(Nada)
    assert "'NoneType' object has no attribute 'upper'" in str(ErrorInfo.value)
    
    assert decodeForJSON('TrUe') == True
    assert decodeForJSON('true ') != True

    assert decodeForJSON('false') == False
    assert decodeForJSON(' false ') != False
 
    assert decodeForJSON('0') == 0
    assert decodeForJSON('+0') == 0
    assert decodeForJSON('-0') == 0
    assert decodeForJSON('1') == 1
    assert decodeForJSON('+1') == 1
    assert decodeForJSON('-1') == -1
    assert decodeForJSON('+034') == 34
    assert decodeForJSON('+034') == 34
    assert decodeForJSON('9223372036854775807') == 9223372036854775807
    assert decodeForJSON('9223372036854775808') == 9223372036854775808
    assert decodeForJSON('+') != 0
    assert decodeForJSON('-') != 0
    assert decodeForJSON('12E4') != 12e4
    assert decodeForJSON('0B11') != 0B11
    assert decodeForJSON('0o11') != 0O11
    assert decodeForJSON('0X11') != 0X11

    assert decodeForJSON('.0') == 0
    assert decodeForJSON('-.0') == 0
    assert decodeForJSON('+.0') == 0
    assert decodeForJSON('123.456') == 123.456
    assert decodeForJSON('123.0') == 123
    assert decodeForJSON('-123.0') == -123
    assert decodeForJSON('+123.0') == 123
    assert decodeForJSON('0.456') == 0.456
    assert decodeForJSON('-0.456') == -0.456
    assert decodeForJSON('+0.456') == 0.456
    assert decodeForJSON('1797693134862315700000000000') == 1797693134862315700000000000
    assert decodeForJSON('.000000000022250738585072014') == .000000000022250738585072014

    assert decodeForJSON('2+3j') == '2+3j'
    
    assert decodeForJSON('abc') == 'abc'

    assert decodeForJSON('a+b') != 'a b'
    assert decodeForJSON('a%20b') != 'a b'
    assert decodeForJSON('a%2Bb') != 'a+b'

    #"
    #\
    #/
    #b
    #f
    #n
    #r
    #t
    #u