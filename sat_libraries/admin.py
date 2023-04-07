import json
from flask import redirect, request
from sat_libraries import functions


def DeleteOneSatelliteByAdmin(SatelliteID):
    data = functions.get_satellites_data()
    result = {"satellites": ""}
    for key, value in enumerate(data):
        if (value['satID'] == SatelliteID):
            data.pop(key)
    result['satellites'] = data
    with open('../satellites.json', 'w') as file:
        json.dump(result, file)

def DeleteOneSatelliteByAdmin(SatelliteName):
    data = functions.get_requests()
    for key, value in enumerate(data):
        if (value['satNAME'] == SatelliteName):
            data.pop(key)

    with open('requests.json', 'w') as file:
        json.dump(data, file)

def add_satellite_admin():
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

    with open('satellites.json', 'r') as f:
        satellites = json.load(f)

    parsed_satellites = satellites['satellites']

    if (functions.collision_detection(data)):
        new_satellite = {
            'satID': max([sat['satID'] for sat in parsed_satellites]) + 1,
            **data
        }
        parsed_satellites.append(new_satellite)
        with open('satellites.json', 'w') as f:
            json.dump({'satellites': parsed_satellites}, f, indent=2)
        print("Request sent successfully!")
    else:
        print("Request failed!")

    return redirect('/admin')





def accept_satellite(sat_name):
    requests = functions.get_requests()
    data = {}
    for satellite in requests:
        if satellite["satNAME"] == sat_name:
            data = satellite
            break

    with open('satellites.json', 'r') as f:
        satellites = json.load(f)

    parsed_satellites = satellites['satellites']

    if (functions.collision_detection(data)):
        new_satellite = {
            'satID': max([sat['satID'] for sat in parsed_satellites]) + 1,
            **data
        }
        parsed_satellites.append(new_satellite)
        with open('satellites.json', 'w') as f:
            json.dump({'satellites': parsed_satellites}, f, indent=2)
        print("Satellite accepted!")
        DeleteOneSatelliteByAdmin(sat_name)
    else:
        print("Process failed!")

    return redirect('/admin')