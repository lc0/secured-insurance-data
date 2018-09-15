from flask import Flask, jsonify
from random import randint
import datetime, urllib, json, codecs, random, time, requests

members = ['ali', 'fredrico', 'gabriel', 'sergei']

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

def postClient():
	url = 'http://8732a407.ngrok.io/api/InsuredClient'
	r = requests.post(url, json={'name': 'aliabbasjaffri', 'id' : 1500, 'age' : 25})
	print(r.status_code)
	return str(r.status_code)

def getInsurer():
	insurers = []
	url = 'http://8732a407.ngrok.io/api/Insurance/123'
	response = urllib.urlopen(url)
	reader = codecs.getreader("utf-8")
	# return json.load(reader(response))
	insurers.append(json.load(reader(response))['id'])
	return insurers

def getClient():
	url = 'http://8732a407.ngrok.io/api/InsuredClient/123'
	response = urllib.urlopen(url)
	reader = codecs.getreader("utf-8")
	# return json.load(reader(response))
	return json.load(reader(response))['id']

@app.route("/health")
def postHealthMeasurement():

	print(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000'))

	url = 'http://8732a407.ngrok.io/api/HealthMeasurement'
	r = requests.post(url, json={ 'heartRate': randint(60, 150), 'numberOfStepsInInterval' : randint(1, 10), 
		'datetimeBeginStepsInterval' : datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000'), 
		'datetimeEndStepsInterval' : datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000'),
		'id' : str(int(time.time())), 'viewers' : getInsurer(), 'ownerId' : getClient() })
	print(r.status_code)
	return str(r.status_code)
