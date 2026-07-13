from flask import Flask, request
from NetflixTrial import get_cookies, build_cookie_string, send_trial_offer

app = Flask(__name__)
@app.route("/")
def home():
    return {
        "status": "online",
        "message": "Server is running"
    }
@app.route("/send", methods=["POST"])
def send():
    email = request.json["email"]

    cookies, _ = get_cookies()
    if not cookies:
        return {"success": False, "message": "Cookie service unavailable"}

    cookie_string = build_cookie_string(cookies)
    results, success = send_trial_offer(email, cookie_string)

    return {
        "success": success,
        "results": results
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
