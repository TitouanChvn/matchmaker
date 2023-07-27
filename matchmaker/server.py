from flask import Flask, send_file, request, jsonify
from flask_cors import CORS,cross_origin

import matchmaker 
import os
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def default():
    return "<p>Hello, World!!</p>"

@app.route('/get_players')
@cross_origin()
def get_players():
    path = "players.json"
    return send_file(path, as_attachment=True)
    


if __name__ == '__main__':
    app.run(debug=True)



