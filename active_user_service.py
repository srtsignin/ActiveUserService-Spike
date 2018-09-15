from flask import Flask
from flask import request
import json

app = Flask(__name__)

active_users = set()

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def handle_request():
    global active_users
    if request.method == 'GET':
        response = {
            'activeUsers': list(active_users)
        }
        return json.dumps(response)
    if request.method == 'POST':
        active_users.add(request.form.get('user'))
        user = request.form.get('user')
        response = {
            'userAdded': user,
            'activeUsers': list(active_users)
        }
        return json.dumps(response)
    active_users.clear()
    response = {
        'result': 'Success',
        'activeUsers': list(active_users)
    }
    return json.dumps(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=65001)