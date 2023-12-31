"""Python Flask App."""

import datetime
import typing

from flask import Flask, jsonify, request

from birthday_demo import datastore, utils

app = Flask(__name__)


@app.route('/hello/<username>', methods=['GET', 'PUT'])
def endpoint(username: str) -> tuple[typing.Any, int]:
    """Process a username endpoint request.

    Parameter:
        username (str): A string containing only letters

    Returns:
        An HTTP response
    """
    errors = {}

    # valiadate imput
    if not username.isalpha():
        errors['INVALID_USERNAME'] = "Please supply a 'username' containing only letters"

    if request.method == 'PUT':
        dob_str = request.args.get('dateOfBirth')
        try:
            datetime.datetime.strptime(dob_str, "%Y-%m-%d")
        except (ValueError, TypeError):
            errors['INVALID_DATE'] = "Please supply 'dateOfBirth' as a valid date in 'YYYY-MM-DD' format"

    if errors:
        return jsonify({'errors': errors}), 400

    # process input
    db = datastore.DB()

    if request.method == 'GET':
        dob_str = db.get_dob(username)
        if not dob_str:
            return jsonify({'message': f'Hello, {username}! you are new, please create an account'}), 404
        days = utils.get_days_to_next_birthday(dob_str)
        if days == 0:
            return jsonify({'message': f'Hello, {username}! Happy birthday!'}), 200
        else:
            return jsonify({'message': f'Hello, {username}! Your birthday is in {days} day(s)'}), 200

    elif request.method == 'PUT':
        db.create_or_update(username, dob_str)
        return jsonify({}), 204

    return jsonify({'error': 'We should not have got here'}), 500
