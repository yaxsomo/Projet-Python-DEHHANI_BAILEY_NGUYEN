from sat_libraries import user, admin, functions
from flask import Flask, redirect, request , url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


## Routes :
#######################################

# Route API pour l'utilisateur
@app.route('/user')
def show_user_interface():
    data = user.get_all_satellite_data().json
        # Form
    form_div = '<div style="border: 1px solid black; padding: 10px; width: 100%;text-align: center;">'
    form_div += '<h3>Add a new satellite:</h3>'
    form_div += '<form method="POST" action="/add_satellite_user">'
    form_div += '<label for="name">Satellite name:</label><br>'
    form_div += '<input type="text" id="name" name="name" required><br>'
    form_div += '<label for="date">Launch date:</label><br>'
    form_div += '<input type="date" id="date" name="date" required><br>'
    form_div += '<label for="apo">Apogee:</label><br>'
    form_div += '<input type="number" id="apo" name="apo" required><span>&#176;</span><br>'
    form_div += '<label for="ecc">Eccentricity:</label><br>'
    form_div += '<input type="number" step="0.01" id="ecc" name="ecc" required><span>&#176;</span><br>'
    form_div += '<label for="inc">Inclination:</label><br>'
    form_div += '<input type="number" id="inc" name="inc" required><span>&#176;</span><br>'
    form_div += '<label for="per">Perigee:</label><br>'
    form_div += '<input type="number" id="per" name="per" required><span>&#176;</span><br>'
    form_div += '<label for="long">Longitude:</label><br>'
    form_div += '<input type="number" step="0.01" id="long" name="long" required><span>&#176;</span><br>'
    form_div += '<label for="pos">Position:</label><br>'
    form_div += '<input type="text" id="pos" name="pos" required><span>&#176;</span><br><br>'
    form_div += '<input type="submit" value="Submit">'
    form_div += '</form></div>'
    
    #Metriques
    num_sat, metrics = functions.calculate_satellite_metrics(data['satellites'])
    apo_min = metrics['satAPO']['min']
    apo_max = metrics['satAPO']['max']
    apo_mean = metrics['satAPO']['mean']
    ecc_min = metrics['satECC']['min']
    ecc_max = metrics['satECC']['max']
    ecc_mean = metrics['satECC']['mean']
    inc_min = metrics['satINC']['min']
    inc_max = metrics['satINC']['max']
    inc_mean = metrics['satINC']['mean']
    per_min = metrics['satPER']['min']
    per_max = metrics['satPER']['max']
    per_mean = metrics['satPER']['mean']
    long_min = metrics['satLONG']['min']
    long_max = metrics['satLONG']['max']
    long_mean = metrics['satLONG']['mean']
    pos_min = metrics['satPOS']['min']
    pos_max = metrics['satPOS']['max']
    pos_mean = metrics['satPOS']['mean']
    
    metrics_display = '<div style="border: 1px solid black; padding: 10px; width:100%;">'
    metrics_display += f'<h3>Satellites Metrics</h3>'
    metrics_display += f'<p><strong>Number of satellites in orbit:</strong> {num_sat}</p>'
    metrics_display += f'<p><strong>Apopsis data:</strong> MIN: {apo_min} | MAX: {apo_max} | MEAN: {apo_mean}</p>'
    metrics_display += f'<p><strong>Ecentricity data:</strong> MIN: {ecc_min} | MAX: {ecc_max} | MEAN: {ecc_mean}</p>'
    metrics_display += f'<p><strong>Inclination data:</strong> MIN: {inc_min} | MAX: {inc_max} | MEAN: {inc_mean}</p>'
    metrics_display += f'<p><strong>Periopsis data:</strong> MIN: {per_min} | MAX: {per_max} | MEAN: {per_mean}</p>'
    metrics_display += f'<p><strong>Longitude data:</strong> MIN: {long_min} | MAX: {long_max} | MEAN: {long_mean}</p>'
    metrics_display += f'<p><strong>Position data:</strong> MIN: {pos_min} | MAX: {pos_max} | MEAN: {pos_mean}</p>'
    metrics_display += '<hr>'
    metrics_display += '</div>'



    # Div pour données satellites et form
    content = '<div style="display:flex;">'
    content += '<div style="border: 1px solid black; padding: 10px; width:100%;">'
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
    content += form_div
    content += metrics_display

    content += '</div>'
    return content

#Route: Satellite ID
@app.route('/user/<int:satellite_id>')
def get_satellite_data(satellite_id):
    satellite = user.get_satellite_data(satellite_id).json
    content = '<div style="display:flex;">'
    content += '<div style="border: 1px solid black; padding: 10px; width:100%;">'
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

#Route: Demande d'jout d'un satellite par l'User
@app.route('/add_satellite_user', methods=['POST'])
def add_sat_usr():
    return user.add_satellite_user()

#Route: Ajout d'un satellite par l'Admin
@app.route('/add_satellite_admin', methods=['POST'])
def add_sat_adm():
    return admin.add_satellite_admin()

# Route API pour l'administrateurs
@app.route('/admin' , methods=['POST' , 'GET'])
def show_admin_interface():
    all_satellites = functions.get_satellites_data()
    all_requests = functions.get_requests()

    # Form
    form_div = '<div style="border: 1px solid black; padding: 10px; width: 100%;text-align: center;">'
    form_div += '<h3>Add a new satellite:</h3>'
    form_div += '<form method="POST" action="/add_satellite_admin">'
    form_div += '<label for="name">Satellite name:</label><br>'
    form_div += '<input type="text" id="name" name="name" required><br>'
    form_div += '<label for="date">Launch date:</label><br>'
    form_div += '<input type="date" id="date" name="date" required><br>'
    form_div += '<label for="apo">Apogee:</label><br>'
    form_div += '<input type="number" id="apo" name="apo" required><span>&#176;</span><br>'
    form_div += '<label for="ecc">Eccentricity:</label><br>'
    form_div += '<input type="number" step="0.01" id="ecc" name="ecc" required><span>&#176;</span><br>'
    form_div += '<label for="inc">Inclination:</label><br>'
    form_div += '<input type="number" id="inc" name="inc" required><span>&#176;</span><br>'
    form_div += '<label for="per">Perigee:</label><br>'
    form_div += '<input type="number" id="per" name="per" required><span>&#176;</span><br>'
    form_div += '<label for="long">Longitude:</label><br>'
    form_div += '<input type="number" step="0.01" id="long" name="long" required><span>&#176;</span><br>'
    form_div += '<label for="pos">Position:</label><br>'
    form_div += '<input type="text" id="pos" name="pos" required><span>&#176;</span><br><br>'
    form_div += '<input type="submit" value="Submit">'
    form_div += '</form></div>'

    #Requetes
    form_div += '<div style="border: 1px solid black; padding: 10px; width: 100%;text-align: center;">'
    form_div += '<h2>Requêtes des utilisateurs :</h2>'
    for request in all_requests:
        form_div += '<p>Satellite Name: {}</p>'.format(request['satNAME'])
        form_div += '<p>Launch Date: {}</p>'.format(request['launchDate'])
        form_div += '<p>Apogee: {}</p>'.format(request['satAPO'])
        form_div += '<p>Eccentricity: {}</p>'.format(request['satECC'])
        form_div += '<p>Inclination: {}</p>'.format(request['satINC'])
        form_div += '<p>Perigee: {}</p>'.format(request['satPER'])
        form_div += '<p>Longitude: {}</p>'.format(request['satLONG'])
        form_div += '<p>Position: {}</p>'.format(request['satPOS'])
        form_div += f'<form action="/accept_satellite/{request["satNAME"]}" method="POST">'
        form_div += '<input type="submit" value="Accept">'
        form_div += '</form>'
        form_div += f'<form action="/deny_satellite/{request["satNAME"]}" method="POST">'
        form_div += '<input type="submit" value="Deny">'
        form_div += '</form>'
        form_div += '<hr>'
    form_div += '</div>'

    #Div pour données satellites, le form d'ajout et les requetes
    content_div = '<div style="display:flex;">'
    content_div += '<div style="border: 1px solid black; padding: 10px; width:100%;">'
    content_div += '<h2>Liste des satellites :</h2>'
    for satellite in all_satellites:
        content_div += '<p>{}</p>'.format(satellite['satNAME'])
        content_div += '<p>Launch Date: {}</p>'.format(satellite['launchDate'])
        content_div += '<p>Apogee: {}</p>'.format(satellite['satAPO'])
        content_div += '<p>Eccentricity: {}</p>'.format(satellite['satECC'])
        content_div += '<p>Inclination: {}</p>'.format(satellite['satINC'])
        content_div += '<p>Perigee: {}</p>'.format(satellite['satPER'])
        content_div += '<p>Longitude: {}</p>'.format(satellite['satLONG'])
        content_div += '<p>Position: {}</p>'.format(satellite['satPOS'])
        content_div += f'<form action="/delete_satellite/{satellite["satID"]}" method="POST">'
        content_div += '<input type="submit" value="Delete">'
        content_div += '</form>'
        content_div += '<hr>'
    content_div += '</div>'
    content_div += form_div
    content_div += '</div>'


    return content_div

#Route : Suppression d'un satellite
@app.route('/delete_satellite/<int:satellite_id>' , methods=['POST'])
def Delete_satellite(satellite_id):
    admin.DeleteOneSatelliteByAdmin(satellite_id)
    return redirect(url_for('show_admin_interface'))

#Route : Refus de demande d'ajout du satellite
@app.route('/deny_satellite/<string:satellite_name>' , methods=['POST'])
def Deny_satellite(satellite_name):
    admin.DeleteOneSatelliteByAdmin(satellite_name)
    return redirect(url_for('show_admin_interface'))

#Route : Acceptation de demande d'ajout du satellite
@app.route('/accept_satellite/<string:satellite_name>' , methods=['POST'])
def Accept_satellite(satellite_name):
    admin.accept_satellite(satellite_name)
    return redirect(url_for('show_admin_interface'))


if __name__ == '__main__':
    app.run()