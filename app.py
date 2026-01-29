from flask import Flask, request, jsonify
from users import UserStorage
from utils import hash_password, check_password

app = Flask(__name__)
users = UserStorage("users.json")


@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return {"error": "username and password required"}, 400

    if users.exists(data["username"]):
        return {"error": "user already exists"}, 400

    password_hash = hash_password(data["password"])
    users.add(data["username"], password_hash)

    return {"status": "registered"}, 201


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if not data:
        return {"error": "invalid request"}, 400

    user = users.get(data.get("username"))
    if not user:
        return {"error": "user not found"}, 404

    if not check_password(data.get("password"), user["password"]):
        return {"error": "wrong password"}, 401

    return {"status": "logged in"}, 200


if __name__ == "__main__":
    app.run(debug=True)
