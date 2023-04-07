import os
from flask import jsonify, redirect, request
from sat_libraries import functions
import json



def get_satellite_data(satellite_id):
    satellites = functions.get_satellites_data()
    for satellite in satellites:
        if satellite['satID'] == satellite_id:
            return jsonify(satellite)
    return jsonify({"error": "Invalid satellite ID"}), 404

    

def get_all_satellite_data():
    satellites = functions.get_satellites_data()
    return jsonify({"satellites": satellites})


def add_satellite_user():
    data = {
        'satNAME': request.form['name'],
        'launchDate': request.form['date'],
        'satAPO': float(request.form['apo']),
        'satECC': float(request.form['ecc']),
        'satINC': float(request.form['inc']),
        'satPER': float(request.form['per']),
        'satLONG': float(request.form['long']),
        'satPOS': float(request.form['pos'])
    }
    satellites = []

    # Check if requests.json exists and load existing data
    if os.path.exists('requests.json'):
        with open('requests.json', 'r') as f:
            file_data = f.read()
            if file_data:
                satellites = json.loads(file_data)

    if(functions.collision_detection(data)):
        satellites.append(data)
        with open('requests.json', 'w') as f:
            json.dump(satellites, f)
        print("Request sent successfully!")  
    else:
        print("Request failed!")
    
    return redirect('/user')
