import json
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




def AddSatelliteByAdmin(name , launchDate , satAPO , satECC , satINC , satPER ,satLONG , satPOS):  # name , launchDate , satAPO , satECC , satINC , satPER ,satLONG , satPOS):
    id = functions.get_maxId() +1
    data = list(functions.get_satellites_data())

    date = datetime.strptime(launchDate, "%Y-%m-%d")
    result = {"satellites" : data}

    # print(len(result['satellites']))
    new_satellite = {"satID": id, "satNAME": name + str(id), "launchDate": date.strftime("%Y-%m-%d"), "satAPO": satAPO, "satECC":satECC, "satINC": satINC, "satPER": satPER, "satLONG": satLONG, "satPOS": satPOS}

    result['satellites'].append(new_satellite)
    # print(len(result['satellites']) , result)

    with open('../satellites.json', 'w') as file:
        json.dump(result, file)

def UpdateSatelliteByAdmin(name , new_name , launchDate , satAPO , satECC , satINC , satPER ,satLONG , satPOS):
    data = functions.get_satellites_data()
    # print(data)
    date = datetime.strptime(launchDate, "%Y-%m-%d")
    for key, value in enumerate(data):
        if (value['satNAME'] == name):
            value['satNAME'] = new_name
            value['launchDate'] = date.strftime("%Y-%m-%d")
            value['satAPO'] = satAPO
            value['satECC'] = satECC
            value['satINC'] = satINC
            value['satPER'] = satPER
            value['satLONG'] = satLONG
            value['satPOS'] = satPOS

    result = {"satellites": data}
    with open('../satellites.json', 'w') as file:
        json.dump(result, file)




#AddSatelliteByAdmin("Sat", "2001-04-27", 1.7, 0.4, 163.9, 263.3, 268.3, 185.2)
#DeleteOneSatelliteByAdmin(9)
#UpdateSatelliteByAdmin("Sat22" , "Sat" ,"2001-04-27", 1.7, 0.4, 163.9, 263.3, 268.3, 185.2)
