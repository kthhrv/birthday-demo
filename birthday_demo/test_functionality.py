from flask import Flask

from .app import app

def test_create_user():
    response = app.test_client().put('/hello/auser?dateOfBirth=2020-01-01')
    assert response.status_code == 204
