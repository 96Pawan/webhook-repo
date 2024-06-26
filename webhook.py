from flask import Flask, request, jsonify, send_from_directory
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['webhook_db']
collection = db['webhook_collection']

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    data['timestamp'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    collection.insert_one(data)
    return jsonify({"message": "Webhook received!"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data), 200

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
