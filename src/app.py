from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details', methods=['GET'])
def hello_world():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hostname = socket.gethostname()
    return jsonify({'time': current_time, 'hostname': hostname}), 200, {'Content-Type': 'application/json; charset=utf-8', 'Indent': '4'}

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'up'}), 200

# main driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0")