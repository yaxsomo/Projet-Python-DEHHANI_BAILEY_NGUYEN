from flask import Flask, jsonify
import random
import datetime
import json

app = Flask(__name__)

num_satellites = 50
# Génération de données aléatoires pour chaque satellite
def generate_satellite_data(satellite_id):
    launch_date = datetime.date(year=random.randint(2000, 2023), month=random.randint(1, 12), day=random.randint(1, 28))
    data = {
        "satID": int(satellite_id),
        "satNAME": "Sat" + str(satellite_id),
        "launchDate": str(launch_date),
        "satAPO": round(random.uniform(1, 6), 1),
        "satECC": round(random.uniform(0, 1), 1),
        "satINC": round(random.uniform(0, 180), 1),
        "satPER": round(random.uniform(0, 360), 1),
        "satLONG": round(random.uniform(0, 360), 1),
        "satPOS": round(random.uniform(0, 360), 1)
    }
    return data

# Générer des données aléatoires pour les satellites
satellites = {}
for i in range(1, num_satellites+1):
    satellites[i] = generate_satellite_data(i)

# Trier les satellites par ordre de date de lancement
sorted_satellites = sorted(satellites.values(), key=lambda x: datetime.datetime.strptime(x['launchDate'], '%Y-%m-%d'))

# Écrire le JSON dans un fichier
with open('satellites.json', 'w') as f:
    json.dump({'satellites': sorted_satellites}, f)


if __name__ == '__main__':
    app.run()
