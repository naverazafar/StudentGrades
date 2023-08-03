from flask import Flask, request, jsonify, render_template, redirect
import requests

app = Flask(__name__, template_folder='.')

@app.route('/authenticate', methods=["GET"])
def webpage():
    return render_template('templates/home.html')

@app.route('/passcheck', methods=['GET'])
def passcheck():
    return render_template('templates/verify.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    # data = request.get_json()
    # username = data.get('username')
    # password = data.get('password')

    username = request.form["username"]
    password = request.form["password"]

    # Perform authentication checks (e.g. checking against a database)
    if username == 'user' and password == 'pass':
        # If authentication is successful, send an HTTP code to the display service
        response = requests.post('http://34.30.62.87:2000/verify', json={'auth': True}, verify=False)
    
        if response.status_code == 200:
            # return jsonify("message: Authentication successful"), 200
            return response.content
        else:
            return jsonify({'message': 'Error communicating with display service'}), 500
    else:
        return jsonify({'message': 'Authentication failed'}), 401

if __name__ == '__main__':
    app.run(port=9000, host=('0.0.0.0'))