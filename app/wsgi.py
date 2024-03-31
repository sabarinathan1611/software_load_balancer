from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    # Get the hostname of the current server
    hostname = socket.gethostname()
    # Get the IP address corresponding to the hostname
    ip_address = socket.gethostbyname(hostname)
    return f"Load balancing Container ID: {ip_address}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
