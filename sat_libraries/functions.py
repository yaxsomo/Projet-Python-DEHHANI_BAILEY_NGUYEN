import datetime
import json
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TKAgg")


# Recuperer les satellites par ordre aleatoire
def get_satellites_data():
    with open('./satellites.json', 'r') as file:
        data = json.load(file)
    return data['satellites']


def get_maxId():
    data = get_satellites_data()
    All_id = [e['satID'] for e in data]
    return max(All_id)

def calculate_satellite_metrics(satellites):
    
    num_satellites = len(satellites)
    metrics = {}
    
    # Calculate metrics for each parameter
    for param in ["satAPO", "satECC", "satINC", "satPER", "satLONG", "satPOS"]:
        values = [sat[param] for sat in satellites]
        metrics[param] = {
            "max": round(max(values),1),
            "min": round(min(values),1),
            "mean": round(sum(values) / len(values),1)
        }
    
    return num_satellites, metrics


def add_four_to_satPOS(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for satellite in data['satellites']:
        print("sat ID : ", satellite['satID'], "satPOS : ", satellite['satPOS'])
        if satellite['satPOS'] < 356:
            satellite['satPOS'] += 4
            print("sat ID : ", satellite['satID'], "satPOS : ", satellite['satPOS'])
        else:
            satellite['satPOS'] += 4 - 360
            print("sat ID : ", satellite['satID'], "satPOS : ", satellite['satPOS'])

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)