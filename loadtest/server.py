from flask import Flask, jsonify
import threading
import time

app = Flask(__name__)

@app.route('/api')
def api():
    return jsonify(status="ok", message="Hello from molotov test!"), 200

if __name__ == '__main__':
    print("Сервер запущен: http://localhost:5000/api")
    app.run(host='0.0.0.0', port=5000)
