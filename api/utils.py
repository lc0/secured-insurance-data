import datetime
import hashlib
import requests
import uuid


def get_hash(unique_str):
    md5 = hashlib.md5()
    md5.update(unique_str.encode('utf-8'))
    return md5.hexdigest()


def send_to_ledger(predictors, user_id):
    url = 'http://8732a407.ngrok.io/api/PictureMeasurement'

    payload = {
        "$class": "org.example.biznet.PictureMeasurement",
        "predictors": [],
        "datetimeMeasurement": datetime.datetime.now().isoformat(),
        "id": str(uuid.uuid1()),
        "viewers": [],
        "ownerId": user_id
    }

    for predictor in predictors:
        payload['predictors'].append({"key": predictor['prediction_class'],
                                      "probability": predictor['probability']})


    result = requests.post(url, json=payload)
    result.raise_for_status()
