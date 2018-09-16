from flask import Flask, jsonify
from random import randint
from collections import defaultdict
from scipy.stats import truncnorm
import datetime, urllib, json, codecs, random, time, requests,pandas as pd

names = ['anna', 'nachos', 'ronaldo', 'carl', 'ben', 'ali', 'fredrico', 'gabriel', 'sergei', 'ben']
ids = [1,2,3,4,5,6,7,8,9,10]
ages = [12, 34, 32, 55, 21, 23, 22, 26, 32, 28]

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/createClients")
def createClients():
	for name, id, age in zip(names, ids, ages):
		postClient(name, id, age)
	return 'createdClients'

def postClient(name, id, age):
	url = 'http://8732a407.ngrok.io/api/InsuredClient'
	r = requests.post(url, json={'name': name, 'id' : id, 'age' : age})
	return str(r.status_code)

def get_truncated_normal(mean=65, sd=23, low=40, upp=150):
    arrayList = truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd).rvs(450)
    arrayList = arrayList.round().astype(int)
    return arrayList

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

	for id in ids:
		
		heartRateData = get_truncated_normal()
		i = 0

		for day in range(1, 101):
			date = datetime.datetime.now() - datetime.timedelta(days = day)
			date = date.strftime('%Y-%m-%dT%H:%M:%S.000')
			for time in range(1, 4):
				postHealthMeasurement(id, date, heartRateData[i])
				i=i+1
				print('i: ' + str(i))
	return '200 ok'

def postHealthMeasurement(id, date, heartRate):
	print(id)
	print(date)
	url = 'http://8732a407.ngrok.io/api/HealthMeasurement'
	r = requests.post(url, json={ 'heartRate': heartRate, 'numberOfStepsInInterval' : randint(1, 10), 
		'datetimeBeginStepsInterval' : date,
		'datetimeEndStepsInterval' : date,
		'id' : str(int(time.time())), 'viewers' : ['1'], 'ownerId' : id })
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
	
	return json.dumps((dict(appearances)))







