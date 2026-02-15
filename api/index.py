from flask import Flask, request, jsonify
import requests, os
from werkzeug.wrappers import Response

app = Flask(name)

PANNEL_KEY = os.environ.get("PANNEL_KEY")
RC_KEY = os.environ.get("RC_KEY")
BAMBU_KEY = os.environ.get("BAMBU_KEY")

def safe_json(url, params):
try:
r = requests.get(url, params=params, timeout=20)
return r.json()
except:
return {"error": "source api down"}

def clean_response(obj):
if isinstance(obj, dict):
obj.pop("Owner", None)
obj.pop("OWNER", None)
obj.pop("BUY_API", None)
obj.pop("SUPPORT", None)
for k in list(obj.keys()):
clean_response(obj[k])
elif isinstance(obj, list):
for i in obj:
clean_response(i)
return obj

@app.route("/")
def home():
return "API RUNNING"

@app.route("/num")
def num_api():
number = request.args.get("number")
data = safe_json("https://api.paanel.shop/numapi.php",
{"action":"api","key":PANNEL_KEY,"number":number})
return jsonify(clean_response(data))

@app.route("/adh")
def adh_api():
adh = request.args.get("adh")
data = safe_json("https://api.paanel.shop/numapi.php",
{"action":"api","key":PANNEL_KEY,"aadhar":adh})
return jsonify(clean_response(data))

@app.route("/rc")
def rc_api():
rc = request.args.get("rc")
data = safe_json("https://usesirosint.vercel.app/api/rcnum",
{"key":RC_KEY,"rc":rc})
return jsonify(clean_response(data))

@app.route("/bambu")
def bambu_api():
num = request.args.get("number")
data = safe_json("https://Usesir.vercel.app/api/bambu",
{"key":BAMBU_KEY,"num":num})
return jsonify(clean_response(data))

def handler(request):
return Response.from_app(app, request.environ)
