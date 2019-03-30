from flask import Flask, jsonify, request
import flask
import json
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

app = Flask(__name__)


customers = {"eafaeee-asdf" : {"face" : "coco no mato"}} # faces : person_data
# @app.route('/')
# def index():
#     return flask.render_template('./index.html')

@app.route("/customers", methods=['GET'])
def all_customers():
    if request.method == 'GET':
        return jsonify(customers)
    else:
        return "405: Restricted method"

@app.route("/customers/<key>", methods=['GET', 'POST'])
def customer(key):
    if request.method == 'GET':
        return jsonify(customers[key])
    elif request.method == 'POST':
        customers[key] = request.args.get('data', None)
    else:
        return "405: Restricted method"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
