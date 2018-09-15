from flask import Flask, jsonify
from random import randint
import datetime, urllib, json, codecs, random, time, requests

members = ['ali', 'fredrico', 'gabriel', 'sergei']

# cannot figure out why the object doesn't get destroyed at the end of function call
# class healthData:
#     customer_name = random.choice(members)
#     timestamp = datetime.datetime.utcnow()
#     heartbeat = randint(35, 150)

#     @staticmethod
#     def customer_health_data():
#         return jsonify(random.choice(members), datetime.datetime.utcnow(), randint(35, 150))

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

def postClient():
	url = 'http://8732a407.ngrok.io/api/InsuredClient'
	r = requests.post(url, json={'name': 'aliabbasjaffri', 'id' : 1500, 'age' : 25})
	print(r.status_code)

def getInsurer():
	url = 'http://8732a407.ngrok.io/api/Insurance/123'
	response = urllib.urlopen(url)
	reader = codecs.getreader("utf-8")
	return json.load(reader(response))

def getClient():
	url = 'http://8732a407.ngrok.io/api/InsuredClient/123'
	response = urllib.urlopen(url)
	reader = codecs.getreader("utf-8")
	return json.load(reader(response))

@app.route("/health")
def postHealthMeasurement():
	insurer = getInsurer()
	return jsonify({ 'heartRate': randint(60, 150), 'viewer' : insurer,
	 'owner' : getClient(), 'id' : int(time.time()), 'timestamp' : datetime.datetime.utcnow()})
