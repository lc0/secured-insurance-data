from flask import Flask, jsonify
from random import randint, random
import datetime

import random

members = ['ali', 'fredrico', 'gabriel', 'sergei']

class healthData:
    customer_name = random.choice(members)
    timestamp = datetime.datetime.utcnow()
    heartbeat = randint(35, 150)

    @staticmethod
    def customer_health_data():
        return jsonify(random.choice(members), datetime.datetime.utcnow(), randint(35, 150))

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"
§
@app.route("/health")
def health():
	return (healthData().customer_health_data())
