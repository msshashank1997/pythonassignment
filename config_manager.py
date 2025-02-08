import configparser
import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

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

@app.route('/config', methods=['GET'])
def get_config():
    try:
        config = read_config('config.ini')
        config_data = extract_config(config)
        save_to_json(config_data, 'config.json')
        return jsonify(config_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)