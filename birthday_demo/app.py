#!/usr/bin/env python3

import datetime

from flask import Flask, jsonify, request

from birthday_demo import datastore, utils

app = Flask(__name__)


@app.route('/hello/<username>', methods=['GET', 'PUT'])
def endpoint(username: str) -> str:
    '''
    Process a username endpoint request

       Paramerter:
          username (str): A string containing only letters

       Returns:
          An HTTP response
    '''
    errors = {}

    if not username.isalpha():
        errors['INVALID_USERNAME'] = "Please supply a 'username' containing only letters"

    if request.method == 'PUT':
        dob_str = request.args.get('dateOfBirth')
        if not dob_str:
            errors['INVALID_DATE'] = "Please supply 'dateOfBirth' as a valid date in 'YYYY-MM-DD' format"
        else:
            try:
                datetime.datetime.strptime(dob_str, "%Y-%m-%d")
            except ValueError:
                errors['INVALID_DATE'] = "Please supply 'dateOfBirth' as a valid date in 'YYYY-MM-DD' format"

    if errors:
        return jsonify({'errors': errors}), 400

    db = datastore.DB()

    if request.method == 'GET':
        dob = db.get_dob(username)
        if not dob:
            return jsonify({'message': f'Hello, {username}! you are new, please create an account'}), 404
        days = utils.get_days_to_next_birthday(db.get_dob(username))
        if days == 0:
            return jsonify({'message': f'Hello, {username}! Happy birthday!'})
        else:
            return jsonify({'message': f'Hello, {username}! Your birthday is in {days} day(s)'})

    elif request.method == 'PUT':
        db.create_or_update(username, dob_str)
        return jsonify({}), 204
