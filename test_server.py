import requests
import pytest

from server import ServerUtil


BASE_URL = "http://0.0.0.0"
PORT = "9000"
URL = BASE_URL + ":" + PORT

def test_hello_world_without_parameter_status():
    response = requests.get(URL + "/helloworld")
    assert response.status_code == 200


def test_hello_world_without_parameter_header():
    response = requests.get(URL + "/helloworld")
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"

def test_hello_world_without_parameter_content():
    response = requests.get(URL + "/helloworld")
    assert response.content.decode('utf-8') == "Hello Stranger"


def test_hello_world_with_parameter_status():
    response = requests.get(URL + "/helloworld?name=iHaveAName")
    assert response.status_code == 200

def test_hello_world_with_parameter_header():
    response = requests.get(URL + "/helloworld?name=iHaveAName")
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"

def test_hello_world_with_parameter_content():
    response = requests.get(URL + "/helloworld?name=iHaveAName")
    assert response.content.decode('utf-8') == "Hello i Have A Name"


def test_versionz_status_code():
    response = requests.get(URL + "/versionz")
    assert response.status_code == 200

def test_versionz_content_type():
    response = requests.get(URL + "/versionz")
    assert response.headers["Content-Type"] == "application/json"


def test_server_util_camel_case_split():
	data = "iAmTesting"

	assert ServerUtil.split_on_camel_case(data) == "i Am Testing"