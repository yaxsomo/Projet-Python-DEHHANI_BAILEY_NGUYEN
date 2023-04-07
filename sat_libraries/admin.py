import json
import os

from flask import redirect, request
from sat_libraries import functions
from datetime import datetime


def DeleteOneSatelliteByAdmin(SatelliteID):
    data = functions.get_satellites_data()
    result = {"satellites": ""}
    for key, value in enumerate(data):
        if (value['satID'] == SatelliteID):
            data.pop(key)
            print(key, value)
    result['satellites'] = data

    print(len(data) , result)
    #print("OUI" , newdata , "OUIi" , len(data))
    with open('../satellites.json', 'w') as file:
        json.dump(result, file)

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
    
    return redirect('/admin')


# def AddSatelliteByAdmin(name , launchDate , satAPO , satECC , satINC , satPER ,satLONG , satPOS):  # name , launchDate , satAPO , satECC , satINC , satPER ,satLONG , satPOS):
#     id = functions.get_maxId() +1
#     data = list(functions.get_satellites_data())

#     date = datetime.strptime(launchDate, "%Y-%m-%d")
#     result = {"satellites" : data}

#     # print(len(result['satellites']))
#     new_satellite = {"satID": id, "satNAME": name + str(id), "launchDate": date.strftime("%Y-%m-%d"), "satAPO": satAPO, "satECC":satECC, "satINC": satINC, "satPER": satPER, "satLONG": satLONG, "satPOS": satPOS}

#     result['satellites'].append(new_satellite)
#     # print(len(result['satellites']) , result)

#     with open('../satellites.json', 'w') as file:
#         json.dump(result, file)

# def UpdateSatelliteByAdmin(name , new_name , launchDate , satAPO , satECC , satINC , satPER ,satLONG , satPOS):
#     data = functions.get_satellites_data()
#     # print(data)
#     date = datetime.strptime(launchDate, "%Y-%m-%d")
#     for key, value in enumerate(data):
#         if (value['satNAME'] == name):
#             value['satNAME'] = new_name
#             value['launchDate'] = date.strftime("%Y-%m-%d")
#             value['satAPO'] = satAPO
#             value['satECC'] = satECC
#             value['satINC'] = satINC
#             value['satPER'] = satPER
#             value['satLONG'] = satLONG
#             value['satPOS'] = satPOS

#     result = {"satellites": data}
#     with open('../satellites.json', 'w') as file:
#         json.dump(result, file)




#AddSatelliteByAdmin("Sat", "2001-04-27", 1.7, 0.4, 163.9, 263.3, 268.3, 185.2)
#DeleteOneSatelliteByAdmin(9)
#UpdateSatelliteByAdmin("Sat22" , "Sat" ,"2001-04-27", 1.7, 0.4, 163.9, 263.3, 268.3, 185.2)
