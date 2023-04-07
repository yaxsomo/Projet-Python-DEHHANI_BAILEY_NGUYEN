import json



JSON_FILE_PATH = '../satellites.json'

# Recuperer les satellites par ordre aleatoire
def get_satellites_data():
    with open(JSON_FILE_PATH, 'r') as file:
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


def add_four_to_satPOS():
    with open(JSON_FILE_PATH, 'r') as file:
        data = json.load(file)

    for satellite in data['satellites']:
        print("sat ID : ", satellite['satID'], "satPOS : ", satellite['satPOS'])
        if satellite['satPOS'] < 356:
            satellite['satPOS'] += 4
            print("sat ID : ", satellite['satID'], "satPOS : ", satellite['satPOS'])
        else:
            satellite['satPOS'] += 4 - 360
            print("sat ID : ", satellite['satID'], "satPOS : ", satellite['satPOS'])

    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)


def collision_detection(json_obj):

    # Load the JSON file into a Python object
    with open(JSON_FILE_PATH) as f:
        data = json.load(f)
    
    # Iterate over the list of satellites in the JSON object
    for sat in data["satellites"]:
        # Check if the value of "satECC" matches the input JSON object
        if float(sat["satECC"]) == float(json_obj["satECC"]):
            print("There is a possible collision ! Please modify the orbite's eccentricity")
            return False
        if sat["satNAME"] == json_obj["satNAME"]:
            print("There is a possible collision ! Name already taken!")
            return False
        
    print("The path is clear ! Await for admin validation.")
    return True
