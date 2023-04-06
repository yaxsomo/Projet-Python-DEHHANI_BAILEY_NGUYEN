import datetime
import json

# Recuperer les satellites par ordre aleatoire
def get_satellites_data():
    with open('../satellites.json', 'r') as file:
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