from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/connect', methods=['GET'])
def connect():
    response_data = {
        "fetch_after_attempt": False,
        "destination": {
            "trunk": "trmum1b25b5f83ee4d7a607d197g"
        },
        "custom_params": "param1=60299&param2=36623932653138362D363061332D346439642D383837342D6333333166616638373265337C454E7C39353333343635363535&param3=abc",
        "record": True,
        "recording_channels": "dual"
    }

    return jsonify(response_data), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(port=5000)

