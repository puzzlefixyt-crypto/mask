from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Original Keys (Render me Environment Variable me daalna)
PANNEL_KEY = os.environ.get("PANNEL_KEY")
RC_KEY = os.environ.get("RC_KEY")
BAMBU_KEY = os.environ.get("BAMBU_KEY")


# ---- Cleaner Function ----
def clean_response(obj):
    if isinstance(obj, dict):
        # Top level aur nested dono jagah se remove karega
        obj.pop("Owner", None)
        obj.pop("OWNER", None)   # 👈 Yeh add karo
        obj.pop("BUY_API", None)
        obj.pop("SUPPORT", None)

        for key in list(obj.keys()):
            clean_response(obj[key])

    elif isinstance(obj, list):
        for item in obj:
            clean_response(item)

    return obj


# ---- API 1 (Number Search) ----
@app.route("/num")
def num_api():
    number = request.args.get("number")
    if not number:
        return jsonify({"error": "Number required"})

    params = {
        "action": "api",
        "key": PANNEL_KEY,
        "number": number
    }

    r = requests.get("https://api.paanel.shop/numapi.php", params=params)
    data = clean_response(r.json())
    return jsonify(data)


# ---- API 2 (Aadhar Search) ----
@app.route("/aadhar")
def aadhar_api():
    aadhar = request.args.get("aadhar")
    if not aadhar:
        return jsonify({"error": "Aadhar required"})

    params = {
        "action": "api",
        "key": PANNEL_KEY,
        "aadhar": aadhar
    }

    r = requests.get("https://api.paanel.shop/numapi.php", params=params)
    data = clean_response(r.json())
    return jsonify(data)


# ---- API 3 (RC Search) ----
@app.route("/rc")
def rc_api():
    rc = request.args.get("rc")
    if not rc:
        return jsonify({"error": "RC required"})

    params = {
        "key": RC_KEY,
        "rc": rc
    }

    r = requests.get("https://usesirosint.vercel.app/api/rcnum", params=params)
    data = clean_response(r.json())
    return jsonify(data)


# ---- API 4 (Bambu Search) ----
@app.route("/bambu")
def bambu_api():
    num = request.args.get("number")
    if not num:
        return jsonify({"error": "Number required"})

    params = {
        "key": BAMBU_KEY,
        "num": num
    }

    r = requests.get("https://Usesir.vercel.app/api/bambu", params=params)
    data = clean_response(r.json())
    return jsonify(data)

# ---- Wakeup / Health Route ----
@app.route("/")
def home():
    return "API RUNNING", 200

@app.route("/ping")
def ping():
    return "OK", 200

if __name__ == "__main__":
    app.run()
