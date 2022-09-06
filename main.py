import math
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


@app.route("/campo", methods=["POST"])
def campo():
  viscocidad = request.json['viscocidad']
  velocidad = request.json['velocidad']
  api = request.json['api']

  p = (141.5/(131.5 + api)) * 8.33
  d = math.sqrt(18 * viscocidad * velocidad) / (9.8 * (8.33 - p))

  response = jsonify(resultado=d)
  response.headers.add("Access-Control-Allow-Origin", "*")
  return response

@app.route('/public/<path>')
def send_report(path):
    return send_from_directory('public', path)