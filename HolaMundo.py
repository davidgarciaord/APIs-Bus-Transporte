import requests
from flask import Flask, jsonify
from opengateway_sandbox_sdk import SimSwap, NumberVerification

app = Flask(__name__)

client_id = "d68ae5b3-fc8b-449d-866f-05f2e2d143f2"
client_secret = "02c5eefa-0fcc-4d86-86b4-56f17e60d2bf"

if __name__ == '__main__':
    app.run(debug=True)
