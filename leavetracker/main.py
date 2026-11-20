import os
from flask import Flask, jsonify

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "dev")

EMPLOYEES = {
    "e1": {"name": "Asha Rao", "annual": 20, "used": 5},
    "e2": {"name": "Liam Chen", "annual": 15, "used": 15},
    "e3": {"name": "Sofia Diaz", "annual": 25, "used": 0},
}


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/version")
def version():
    return jsonify(version=VERSION)


@app.route("/leave/<eid>")
def balance(eid):
    emp = EMPLOYEES.get(eid)
    if not emp:
        return jsonify(error="Employee not found"), 404
    return jsonify(id=eid, remaining=emp["annual"] - emp["used"], **emp)