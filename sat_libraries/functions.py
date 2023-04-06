import datetime
import json

# Recuperer les satellites par ordre aleatoire
def get_satellites_data():
    with open('satellites.json', 'r') as file:
        data = json.load(file)
    return data['satellites']

