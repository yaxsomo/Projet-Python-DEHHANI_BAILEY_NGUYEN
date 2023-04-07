import datetime
import json
import math


# Recuperer les satellites par ordre aleatoire
def get_satellites_data():
    with open('./satellites.json', 'r') as file:
        data = json.load(file)
    return data['satellites']


def get_maxId():
    data = get_satellites_data()
    All_id = [e['satID'] for e in data]
    return max(All_id)

def test(satellite):
    # Generate orbit plot
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = satellite['satPOS'] * np.outer(np.cos(u), np.sin(v))
    y = satellite['satPOS'] * np.outer(np.sin(u), np.sin(v))
    z = satellite['satPOS'] * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='b')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.title(f"Orbit plot for {satellite['satNAME']}")
    return fig

def calculate_satellite_speed(satellite_data):
    # Gravitational parameter of Earth (m^3/s^2)
    mu = 3.986e14
    
    # Calculate the distance between the center of the Earth and the satellite at periapsis
    a = satellite_data["satAPO"]
    e = satellite_data["satECC"]
    r = (1 - e) * a
    
    # Calculate the velocity of the satellite
    velocity = math.sqrt(mu / r)
    
    return velocity

    