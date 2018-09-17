from flask import Flask, jsonify
from random import randint
from collections import defaultdict
import datetime, urllib, json, codecs, random, time, requests,pandas as pd
from flask_cors import CORS

members = ['ali', 'fredrico', 'gabriel', 'sergei']

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Index Page"

def postClient():
	url = 'http://8732a407.ngrok.io/api/InsuredClient'
	r = requests.post(url, json={'name': 'aliabbasjaffri', 'id' : 1500, 'age' : 25})
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
def postLoadsData():
	for day in range(1, 101):
		date = datetime.datetime.now() - datetime.timedelta(days = day)
		date = date.strftime('%Y-%m-%dT%H:%M:%S.000')
		for time in range(1, 4):
			postHealthMeasurement(date)

def postHealthMeasurement(date):
	print(date)
	url = 'http://8732a407.ngrok.io/api/HealthMeasurement'
	r = requests.post(url, json={ 'heartRate': randint(60, 150), 'numberOfStepsInInterval' : randint(1, 10), 
		'datetimeBeginStepsInterval' : date,
		'datetimeEndStepsInterval' : date,
		'id' : str(int(time.time())), 'viewers' : getInsurer(), 'ownerId' : getClient() })
	print(r.status_code)
	return str(r.status_code)

@app.route("/getImageCategories")
def getImageCategories():
	r = requests.get('http://8732a407.ngrok.io/api/PictureMeasurement')
	pictures = r.json()
	
	pics = []
	for j in pictures:
		pics.append(str(j['predictors'][0]['key']))

	appearances = defaultdict(int)

	for curr in pics:
		appearances[curr] += 1
	reader = codecs.getreader("utf-8")

	app_dict = dict(appearances)
	list_headers=[]
	list_counts=[]
	for k,v in app_dict.items():
		print k,v
		list_headers.append(k)
		list_counts.append(v)

	
	return json.dumps(
		{'headers':list_headers,
		'counts':list_counts})


if __name__=='__main__':
    app.run(debug=True, port=5000)




