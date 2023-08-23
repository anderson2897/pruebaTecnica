import requests
from flask import jsonify


def getInformationAPI(external_url, TOKEN):
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + TOKEN
    }
    response = requests.request("GET", external_url, headers=headers)
    data = response.json()
    return jsonify(data), response.status_code


