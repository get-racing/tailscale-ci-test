#!/usr/bin/env python

from flask import Flask, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def catch_all(path):
    print()
    print()

    print(f"Received request: {request.method} {request.url}")
    # print(f"Request headers: {request.headers}")
    print(f"Request body: {request.get_data(as_text=True)}")

    print()

    return "Request received!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
