from flask import jsonify
from sat_libraries import functions
import json

satellites = functions.get_satellites_data()

def get_satellite_data(satellite_id):
    for satellite in satellites:
        if satellite['satID'] == satellite_id:
            return jsonify(satellite)
    return jsonify({"error": "Invalid satellite ID"}), 404

    

def get_all_satellite_data():
    return jsonify({"satellites": satellites})

