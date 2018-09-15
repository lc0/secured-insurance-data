from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
import json
from flask import Flask, request, render_template, jsonify, redirect

import psycopg2

from utils import get_hash, send_to_ledger

app = Flask(__name__)
working_dir = os.getcwd()


@app.route('/api/save/<user_id>', methods=['POST'])
def save_data(user_id):
    data = request.json

    send_to_ledger(data['predictors'], user_id, data['provider'])

    # TODO: move to a proper place
    db_connection = psycopg2.connect("dbname=postgres user=khomenkos")
    cursor = db_connection.cursor()

    for predictor in data['predictors']:
        # TODO: proper save
        query = """INSERT INTO t_user_interests (a_user_id,
                        a_type,
                        a_interest,
                        a_probability) VALUES ('%s', '%s', '%s', %f)""" % (
                            get_hash(user_id),
                            data['type'],
                            predictor['prediction_class'],
                            predictor['probability'])

        cursor.execute(query)

    db_connection.commit()
    db_connection.close()

    return jsonify({'status': f'pretending to save data for user_id {user_id}'})

if __name__ == "__main__":
    app.debug = True

    app.run(port=8083)
    app.run(debug = True)



if __name__ == "__main__":
    app.debug = True

    app.run(port=8083)
    app.run(debug = True)