from flask import Flask

from .app import app

def test_create_user():
    response = app.test_client().put('/hello/auser?dateOfBirth=2020-01-01')
    assert response.status_code == 204


def test_check_user():
    response = app.test_client().get('/hello/auser')
    assert response.status_code == 200


def test_check_user_does_not_exist():
    response = app.test_client().get('/hello/notauser')
    assert response.status_code == 404
