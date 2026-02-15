import json, os, requests

PANNEL_KEY = os.environ.get("PANNEL_KEY")
RC_KEY = os.environ.get("RC_KEY")
BAMBU_KEY = os.environ.get("BAMBU_KEY")

def clean(obj):
if isinstance(obj, dict):
for k in ["Owner","OWNER","BUY_API","SUPPORT"]:
obj.pop(k, None)
for v in obj.values():
clean(v)
elif isinstance(obj, list):
for i in obj:
clean(i)
return obj

def fetch(url, params):
try:
r = requests.get(url, params=params, timeout=20)
return clean(r.json())
except:
return {"error":"source api down"}

def handler(request):
path = request.path

if path == "/":
    return {
        "statusCode":200,
        "body":"API RUNNING"
    }

if path == "/num":
    number = request.query.get("number")
    data = fetch("https://api.paanel.shop/numapi.php",
                 {"action":"api","key":PANNEL_KEY,"number":number})
    return {"statusCode":200,"body":json.dumps(data)}

if path == "/adh":
    adh = request.query.get("adh")
    data = fetch("https://api.paanel.shop/numapi.php",
                 {"action":"api","key":PANNEL_KEY,"aadhar":adh})
    return {"statusCode":200,"body":json.dumps(data)}

if path == "/rc":
    rc = request.query.get("rc")
    data = fetch("https://usesirosint.vercel.app/api/rcnum",
                 {"key":RC_KEY,"rc":rc})
    return {"statusCode":200,"body":json.dumps(data)}

if path == "/bambu":
    num = request.query.get("number")
    data = fetch("https://Usesir.vercel.app/api/bambu",
                 {"key":BAMBU_KEY,"num":num})
    return {"statusCode":200,"body":json.dumps(data)}

return {"statusCode":404,"body":"Not Found"}
