import configparser
import json
import os
import logging
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

def read_config(file_path):
    config = configparser.ConfigParser()
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file {file_path} not found.")
    
    config.read(file_path)
    return config

def extract_config(config):
    config_data = {}
    for section in config.sections():
        config_data[section] = {}
        for key, value in config.items(section):
            config_data[section][key] = value
    return config_data

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Save data to MongoDB
def save_to_mongo(data):
    try:
        logging.info(f"Data to be saved to MongoDB: {data}")
        if isinstance(data, dict):
            logging.info("Inserting a single document into MongoDB")
            result = mongo.db.configurations.insert_one(data)
            data['_id'] = str(result.inserted_id)
        elif isinstance(data, list):
            logging.info("Inserting multiple documents into MongoDB")
            result = mongo.db.configurations.insert_many(data)
            for i, doc_id in enumerate(result.inserted_ids):
                data[i]['_id'] = str(doc_id)
        logging.info("Data successfully saved to MongoDB")
    except Exception as e:
        logging.error(f"An error occurred while saving to MongoDB: {e}")

@app.route('/config', methods=['GET'])
def get_config():
    # fetch all the data from mongo db
    data = list(mongo.db.configurations.find())
    for item in data:
        item['_id'] = str(item['_id'])  # Convert ObjectId to string
    return jsonify(data)

if __name__ == '__main__':
    try:
        config = read_config('config.ini')
        config_data = extract_config(config)
        save_to_json(config_data, 'config.json')
        save_to_mongo(config_data)  # Ensure this line is present to save data to MongoDB
        print(json.dumps(config_data, indent=4))
    except Exception as e:
        print(json.dumps({"error": str(e)}), 500)
    app.run(debug=True, port=8080)  # Change the port to avoid conflicts