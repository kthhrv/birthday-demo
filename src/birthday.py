#!/usr/bin/env python3

from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route('/hello/<username>', methods=['PUT'])
def create_user(username):
    dob_raw = request.args.get('dateOfBirth')
    dob_parts = dob_raw.split('-')
    try:
        dob = datetime.date(int(dob_parts[0]), int(dob_parts[1]), int(dob_parts[2]))
    except ValueError as exp:
        return jsonify({'error': f'{dob_raw}, {str(exp)}'})

    return jsonify({'name': username, 'dob': dob})


@app.route('/hello/<username>', methods=['GET'])
def check_birthday(username):
    return jsonify({'message': f'Helo, {username}!'})

app.run()
