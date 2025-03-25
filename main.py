import flask
import re

# TODO: change this to your academic email
AUTHOR = "ishimwe@seas.upenn.edu"

app = flask.Flask(__name__)

# This is a simple route to test your server
@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"

# Password validator endpoint
@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    # Check: Length
    if len(pw) < 8:
        return flask.jsonify({"valid": False, "reason": "Password must be at least 8 characters long"}), 400

    # Check: At least 2 uppercase letters
    if len(re.findall(r"[A-Z]", pw)) < 2:
        return flask.jsonify({"valid": False, "reason": "Password must contain at least 2 uppercase letters"}), 400

    # Check: At least 1 digit
    if not re.search(r"\d", pw):
        return flask.jsonify({"valid": False, "reason": "Password must contain at least 1 digit"}), 400

    # Check: At least 1 special character from !@#$%^&*
    if not re.search(r"[!@#$%^&*]", pw):
        return flask.jsonify({"valid": False, "reason": "Password must contain at least 1 special character (!@#$%^&*)"}), 400

    # If all checks pass
    return flask.jsonify({"valid": True, "reason": "Password is valid"}), 200
