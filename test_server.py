import requests
import pytest


def test_hello_world_without_parameter_status():
    response = requests.get("http://0.0.0.0:8080/helloworld")
    assert response.status_code == 200


def test_hello_world_without_parameter_header():
    response = requests.get("http://0.0.0.0:8080/helloworld")
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"

def test_hello_world_without_parameter_content():
    response = requests.get("http://0.0.0.0:8080/helloworld")
    assert response.content.decode('utf-8') == "Hello Stranger"


def test_hello_world_with_parameter_status():
    response = requests.get("http://0.0.0.0:8080/helloworld?name=iHaveAName")
    assert response.status_code == 200

def test_hello_world_with_parameter_header():
    response = requests.get("http://0.0.0.0:8080/helloworld?name=iHaveAName")
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"

def test_hello_world_with_parameter_content():
    response = requests.get("http://0.0.0.0:8080/helloworld?name=iHaveAName")
    assert response.content.decode('utf-8') == "Hello i Have A Name"

