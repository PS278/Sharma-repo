from flask import Flask, jsonify, request
from flask_cors import CORS
import socket
 
app = Flask(__name__)
CORS(app)  # Enable CORS
 
# Main route
@app.route('/', methods=['GET'])
def main():
    return "Welcome to Sharma Final Test API Server."
 
# IP route
@app.route('/ip', methods=['GET'])
def get_ip():
    ip_address = request.remote_addr
    return jsonify({"ip_address": ip_address})
 
# Host route
@app.route('/host', methods=['GET'])
def get_hostname():
    hostname = socket.gethostname()
    return jsonify({"hostname": hostname})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)