from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}   # in-memory user store

@app.route('/')
def home():
    return {"message": "API Running"}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:uid>', methods=['GET'])
def get_user(uid):
    return (jsonify(users[uid]) if uid in users 
            else ({"error": "User not found"}, 404))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    uid = data.get("id")
    if uid in users:
        return {"error": "User ID exists"}, 400
    users[uid] = {"name": data.get("name"), "email": data.get("email")}
    return {"message": "User created", "user": users[uid]}, 201

@app.route('/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    if uid not in users:
        return {"error": "User not found"}, 404
    data = request.json
    users[uid].update({k: v for k, v in data.items() if v is not None})
    return {"message": "Updated", "user": users[uid]}

@app.route('/users/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    if uid not in users:
        return {"error": "User not found"}, 404
    del users[uid]
    return {"message": "Deleted"}

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run()
