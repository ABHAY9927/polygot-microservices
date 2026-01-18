from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/data')
def get_data():
    db_url = os.environ['DATABASE_URL']
    return jsonify({"status": "connected", "db": db_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
