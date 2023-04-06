from flask import jsonify
from sat_libraries import functions

satellites = functions.get_satellites_data()


def get_satellite_data(satellite_id):
    if satellite_id not in satellites:
        return jsonify({"error": "Invalid satellite ID"}), 404
    else:
        data = satellites[satellite_id]
        return jsonify(data)
    

def get_all_satellite_data():
    return jsonify({"satellites": satellites})