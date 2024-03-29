from flask import Flask
import socket
app = Flask(__name__)

@app.route('/')
def home():
     return f"Loadbalacing Container ID :{socket.gethostbyname()} "


if '__main__' == __name__:
    app.run(debug=True,host='0.0.0.0')