from flask import Flask, render_template
import threading
from flask_cors import CORS
import compute as c
import numpy as np

from flask_socketio import SocketIO, send, emit

__version__ = 3

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


def socket_thread():
    global socketio
    socketio.run(app)

    sleep(5)
    send("hello")
    print("message sent")


if __name__ == '__main__':
    threading.Thread(target=socket_thread).start()
    print("started socket app")


    @socketio.on('message')
    def handle_message(message):
        print('received message: ' + message)
        
        
    @socketio.on('form data')
    def handle_my_custom_event(json):
        X = np.array([[json["ageKey"],json["genderKey"],json["cp"],json["rbp"],json["cholKey"],json["fbsKey"],json["restecgKey"],json["thalachKey"],json["exangKey"],json["oldpeakKey"],json["slopeKey"],json["caKey"],json["thalKey"]]])
        """print(X)
        print('received json: ' + str(json))
        print('Answer is : ' + str(c.computeResult(X)))"""
        send(["Result" , str(c.computeResult(X))])
    
    




