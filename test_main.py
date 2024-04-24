from fastapi.testclient import TestClient
from main import app
import re

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Send request to /rates/ with currency code(036, 051, 704, 978 etc.)"}


def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'


def test_predict_get():
    response = client.get("/predict/")
    assert response.status_code == 405
    assert response.json() == {'detail': 'Method Not Allowed'}


def test_rates_post():
    response = client.post("/rates?currency_code=933")
    assert response.status_code == 200
    my_regex = re.compile("1 Белорусский рубль стоит \d+(?:\,\d*) RUB")
    assert my_regex.match(response.json()['message']) is not None
