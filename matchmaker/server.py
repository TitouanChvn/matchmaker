
from flask import Flask, send_file, request, jsonify
from flask_cors import CORS,cross_origin
from flask_socketio import SocketIO, emit
import threading

import matchmaker 
import os
import json

import random as rd
import time


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#socketio = SocketIO(app,async_mode='gevent', cors_allowed_origins="*")




@app.route('/')
@cross_origin()
def default():
    return "<p>Hello, World!!</p>"

@app.route('/get_players')
@cross_origin()
def get_players():
    path = "players.json"
    return send_file(path, as_attachment=True)
    
#@socketio.on('connect')
#def handle_connect():
#    while True:
#        with open('players.json', 'r') as file:
#            data = json.load(file)
#            emit('json_file', data)
#        file.close()
#        time.sleep(5)

#def send_player_list():
    while True:
        with "players.json" as file:
            data = json.load(file)
            socketio.emit('json_file', data)
            print("sent json file")
        file.close()
        socketio.sleep(5)
#def change_random():
#    matchmaker.change_random()

if __name__ == '__main__':
    #update_thread = threading.Thread(target=change_random)
    #update_thread.daemon = True
    #update_thread.start()
    #socketio.start_background_task(send_player_list)
    #socketio.run(app, debug=True)
    
    app.run(debug=True)



