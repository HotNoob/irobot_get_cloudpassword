#!/usr/bin/env python3

import sys
import requests


user = sys.argv[1]
password = sys.argv[2]

if not user or not password:
    print('usage: python get_cloud_password.py "your irobot username" "your irobot password"')



r = requests.get("https://disc-prod.iot.irobotapi.com/v1/discover/endpoints?country_code=US")
response = r.json()
deployment = response['deployments'][next(iter(response['deployments']))]

data = {"apiKey": response['gigya']['api_key'],
        "targetenv": "mobile",
        "loginID": user,
        "password": password,
        "format": "json",
        "targetEnv": "mobile",
}

r = requests.post("https://accounts.%s/accounts.login" % response['gigya']['datacenter_domain'], data=data)

response = r.json()

data = {
    "app_id": "HotNoob Was Here 2024",
    "assume_robot_ownership": "0",
    "gigya": {
        "signature": response['UIDSignature'],
        "timestamp": response['signatureTimestamp'],
        "uid": response['UID'],
    }
}

r = requests.post("%s/v2/login" % deployment['httpBase'], json=data)

response = r.json()
robots = response['robots']
for key, robot in robots.items():
    print("id: " + key + ", name: "+ robot["name"] + ", password: ")
    print(robot["password"])
    print()