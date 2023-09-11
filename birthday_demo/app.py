#!/usr/bin/env python3

import datetime

from flask import Flask, jsonify, request

from . import datastore

app = Flask(__name__)


@app.route('/hello/<username>', methods=['PUT'])
def create_user(username: str) -> str:
    '''
    Process a user creation request.

       Paramerter:
          username (str): A string containing only letters

       Returns:
          An HTTP response
    '''
    errors = {}

    dob_str = request.args.get('dateOfBirth')
    if not dob_str:
        errors['INVALID_DATE'] = "Please supply 'dateOfBirth' as a valid date in 'YYYY-MM-DD' format"
    else:
        try:
            datetime.datetime.strptime(dob_str, "%Y-%m-%d")
        except ValueError:
            errors['INVALID_DATE'] = "Please supply 'dateOfBirth' as a valid date in 'YYYY-MM-DD' format"

    if not username.isalpha():
        errors['INVALID_USERNAME'] = "Please supply a 'username' containing only letters"

    if errors:
        return jsonify({'errors': errors}), 400

    db = datastore.DB()
    db.create_or_update(username, dob_str)

    return jsonify({}), 204


@app.route('/hello/<username>', methods=['GET'])
def check_birthday(username: str) -> str:
    db = datastore.DB()
    days = get_days_to_next_birthday(db.get_dob(username))

    if days == 0:
        return jsonify({'message': f'Hello, {username}! Happy birthday!'})
    else:
        return jsonify({'message': f'Hello, {username}! Your birthday is in {days} day(s)'})


def get_days_to_next_birthday(dob_str):
    today = datetime.date.today()
    dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d")
    birthday = datetime.date(today.year, dob.month, dob.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)

    return (birthday - today).days
