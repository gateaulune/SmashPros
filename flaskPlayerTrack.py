from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_current', methods=['GET'])
def get_current():
    username = request.args.get('username')
    url = f"https://smashpros.gg/api/users/{username}" 
    headers = {'connect.sid':'.'}  # Replace with your specific cookie value
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"status_code": response.status_code, "reason": response.reason})

if __name__ == '__main__':
    app.run(debug=True)