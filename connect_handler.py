from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/connect', methods=['GET'])
def connect():
    response_data = {
        "fetch_after_attempt": False,
        "destination": {
            "trunk": "trmum1b25b5f83ee4d7a607d197g"
        },
        "custom_params": "param1=60299&param2=30303030333031323037313734333435353239313B30393434373931383638353B656E676C697368&param3=abc",
        "record": True,
        "recording_channels": "dual"
    }

    return jsonify(response_data), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(port=5000)
