from sat_libraries import user, admin, functions
from flask import Flask, flash, jsonify, make_response, redirect, render_template, request , url_for
import json
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
## Routes :

# Route API pour l'utilisateur
@app.route('/user')
def show_user_interface():
    data = user.get_all_satellite_data().json
        # Create a div for the form
    form_div = '<div style="border: 1px solid black; padding: 10px; width: 100%;text-align: center;">'
    form_div += '<h3>Add a new satellite:</h3>'
    form_div += '<form method="POST" action="/add_satellite">'
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
    
    num_sat, metrics = functions.calculate_satellite_metrics(data['satellites'])
    print(num_sat, metrics['satAPO']['min'])
    "satAPO", "satECC", "satINC", "satPER", "satLONG", "satPOS"
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



    # Creation d'une div pour afficher les données satellite et le form
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
    # # return satellite
    # fig = functions.test(satellite)
    # output = io.BytesIO()
    # FigureCanvas(fig).print_png(output)
    # return Response(output.getvalue(), mimetype='image/png')
    return content
    
@app.route('/add_satellite', methods=['POST'])
def add_satellite():
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
    
    return redirect('/user')
# Route API pour l'administrateurs

@app.route('/admin' , methods=['POST' , 'GET'])
def show_admin_interface():
    all_satellites = functions.get_satellites_data()

    form_div = '<div style="border: 1px solid black; padding: 10px; width: 100%;text-align: center;">'
    form_div += '<h3>Add a new satellite:</h3>'
    form_div += '<form method="POST" action="/add_satellite">'
    form_div += '<label for="name">Satellite name:</label><br>'
    form_div += '<input type="text" id="name" name="name"><br>'
    form_div += '<label for="date">Launch date:</label><br>'
    form_div += '<input type="date" id="date" name="date"><br>'
    form_div += '<label for="apo">Apogee:</label><br>'
    form_div += '<input type="number" id="apo" name="apo"><span>&#176;</span><br>'
    form_div += '<label for="ecc">Eccentricity:</label><br>'
    form_div += '<input type="number" step="0.01" id="ecc" name="ecc"><span>&#176;</span><br>'
    form_div += '<label for="inc">Inclination:</label><br>'
    form_div += '<input type="number" id="inc" name="inc"><span>&#176;</span><br>'
    form_div += '<label for="per">Perigee:</label><br>'
    form_div += '<input type="number" id="per" name="per"><span>&#176;</span><br>'
    form_div += '<label for="long">Longitude:</label><br>'
    form_div += '<input type="number" step="0.01" id="long" name="long"><span>&#176;</span><br>'
    form_div += '<label for="pos">Position:</label><br>'
    form_div += '<input type="text" id="pos" name="pos"><span>&#176;</span><br><br>'
    form_div += '<input type="submit" value="Submit">'
    form_div += '</form></div>'


    form_div += '<div style="border: 1px solid black; padding: 10px; width: 100%;text-align: center;">'
    form_div += '<h2>Requêtes des utilisateurs :</h2>'
    form_div += '</div>'

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
        content_div += f'<form action="/update_satellite/{satellite["satNAME"]}" method="POST"" method="POST">'
        content_div += f'<input type="hidden" name="id" value="{satellite["satID"]}">'
        content_div += '<input type="submit" value="Update">'
        content_div += '</form>'
        content_div += f'<form action="/delete_satellite/{satellite["satID"]}" method="POST">'
        content_div += '<input type="submit" value="Delete">'
        content_div += '</form>'
        content_div += '<hr>'
    content_div += '</div>'

    #content_div += '<div class="col-md-6">'
    #content_div += '<h2>Requêtes des utilisateurs :</h2>'
    content_div += form_div
    content_div += '</div>'


    return content_div

@app.route('/delete_satellite/<int:satellite_id>' , methods=['POST'])
def Delete_satellite(satellite_id):
    print(satellite_id , "OOOIOO")
    admin.DeleteOneSatelliteByAdmin(satellite_id)
    return redirect(url_for('show_admin_interface'))


@app.route('/update_satellite/<string:satellite_name>' , methods=['POST' , 'GET'])
def Update_satellite(satellite_name):
    form_div = '<div style="border: 1px solid black; padding: 10px; width: 100%;text-align: center;">'
    form_div += f'<h3>Update Satellite: {satellite_name}</h3>'
    form_div += '<form method="POST" action="/admin">'
    form_div += '<label for="name">Satellite name:</label><br>'
    form_div += '<input type="text" id="name" name="name"><br>'
    form_div += '<label for="date">Launch date:</label><br>'
    form_div += '<input type="date" id="date" name="date"><br>'
    form_div += '<label for="apo">Apogee:</label><br>'
    form_div += '<input type="number" id="apo" name="apo"><span>&#176;</span><br>'
    form_div += '<label for="ecc">Eccentricity:</label><br>'
    form_div += '<input type="number" step="0.01" id="ecc" name="ecc"><span>&#176;</span><br>'
    form_div += '<label for="inc">Inclination:</label><br>'
    form_div += '<input type="number" id="inc" name="inc"><span>&#176;</span><br>'
    form_div += '<label for="per">Perigee:</label><br>'
    form_div += '<input type="number" id="per" name="per"><span>&#176;</span><br>'
    form_div += '<label for="long">Longitude:</label><br>'
    form_div += '<input type="number" step="0.01" id="long" name="long"><span>&#176;</span><br>'
    form_div += '<label for="pos">Position:</label><br>'
    form_div += '<input type="text" id="pos" name="pos"><span>&#176;</span><br><br>'
    form_div += '<input type="submit" value="Submit">'
    form_div += '</form></div>'

    name = request.form['name']
    date = request.form['date']
    apo = request.form['apo']
    ecc = request.form['ecc']
    inc = request.form['inc']
    per = request.form['per']
    long = request.form['long']
    pos = request.form['pos']

    admin.UpdateSatelliteByAdmin(satellite_name , name , date , apo , ecc , inc , per , long , pos)

    return form_div



if __name__ == '__main__':
    app.run()