from flask import Flask, request, jsonify
import requests
import os

app = Flask(name)

PANNEL_KEY = os.environ.get("PANNEL_KEY")
RC_KEY = os.environ.get("RC_KEY")
BAMBU_KEY = os.environ.get("BAMBU_KEY")

def clean_response(obj):
if isinstance(obj, dict):
obj.pop("Owner", None)
obj.pop("OWNER", None)
obj.pop("BUY_API", None)
obj.pop("SUPPORT", None)
for key in list(obj.keys()):
clean_response(obj[key])
elif isinstance(obj, list):
for item in obj:
clean_response(item)
return obj

@app.route("/")
def home():
return "API RUNNING"

number

@app.route("/num")
def num_api():
number = request.args.get("number")
params = {"action":"api","key":PANNEL_KEY,"number":number}
r = requests.get("https://api.paanel.shop/numapi.php", params=params)
return jsonify(clean_response(r.json()))

aadhar → adh?adh=

@app.route("/adh")
def adh_api():
adh = request.args.get("adh")
params = {"action":"api","key":PANNEL_KEY,"aadhar":adh}
r = requests.get("https://api.paanel.shop/numapi.php", params=params)
return jsonify(clean_response(r.json()))

@app.route("/rc")
def rc_api():
rc = request.args.get("rc")
params = {"key":RC_KEY,"rc":rc}
r = requests.get("https://usesirosint.vercel.app/api/rcnum", params=params)
return jsonify(clean_response(r.json()))

@app.route("/bambu")
def bambu_api():
num = request.args.get("number")
params = {"key":BAMBU_KEY,"num":num}
r = requests.get("https://Usesir.vercel.app/api/bambu", params=params)
return jsonify(clean_response(r.json()))

handler = app
