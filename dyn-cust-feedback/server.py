import os
from flask import Flask, jsonify, request

import json
from prediction import predict


HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def flask_app():
    app = Flask(__name__)


    @app.route('/healthz', methods=['GET'])
    def healthz():
        message = {"status": "Aal is well!!!"}
        response = jsonify(message)
        response.status_code = 200
        return response

    @app.route('/predict', methods=['POST'])
    def start():
        input_text = request.json
        return jsonify(predict(input_text['text']))
    return app

if __name__ == '__main__':
    app = flask_app()
    app.run(debug=True, host='0.0.0.0', port=3000)
