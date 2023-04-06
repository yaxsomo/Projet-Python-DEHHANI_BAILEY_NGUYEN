from sat_libraries import user, admin
from flask import Flask, jsonify

app = Flask(__name__)

## Routes :

# Route API pour l'utilisateur
@app.route('/user')
# def show_user_interface():
#     return user.get_all_satellite_data()
def show_user_interface():
    data = user.get_all_satellite_data().json
    content = '<div style="border: 1px solid black; padding: 10px; width:50%;">'
    for satellite in data['satellites']:
        content += f'<h3>Satellite Name : {satellite["satNAME"]}</h3>'
        content += f'<p><strong>Satellite ID:</strong> {satellite["satID"]}</p>'
        content += f'<p><strong>Launch Date:</strong> {satellite["launchDate"]}</p>'
        content += f'<p><strong>Apogee:</strong> {satellite["satAPO"]}</p>'
        content += f'<p><strong>Eccentricity:</strong> {satellite["satECC"]}</p>'
        content += f'<p><strong>Inclination:</strong> {satellite["satINC"]}</p>'
        content += f'<p><strong>Perigee:</strong> {satellite["satPER"]}</p>'
        content += f'<p><strong>Logitude:</strong> {satellite["satLONG"]}</p>'
        content += f'<p><strong>Position:</strong> {satellite["satPOS"]}</p>'
        content += '<hr>'
    content += '</div>'
    return content



# Route API pour l'administrateur

# @app.route('/admin')


if __name__ == '__main__':
    app.run()