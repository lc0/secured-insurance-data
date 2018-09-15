##### Visual Search Demo - Image similarity with Inception.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
from flask import Flask, request, render_template, jsonify, redirect

app = Flask(__name__)
working_dir = os.getcwd()


@app.route('/api/save/<user_id>', methods=['POST'])
def save_data(user_id):
    print(request.json)

    return jsonify({'status': f'pretending to save data for user_id {user_id}'})

if __name__ == "__main__":
    app.debug = True

    app.run(port=8083)
    app.run(debug = True)



if __name__ == "__main__":
    app.debug = True

    app.run(port=8083)
    app.run(debug = True)