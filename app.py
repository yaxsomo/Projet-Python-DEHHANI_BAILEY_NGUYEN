from sat_libraries import user, admin, functions
from flask import Flask, jsonify, render_template
import io
from flask import Response
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


app = Flask(__name__)
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


    # Create a div to display the satellite data and form side by side
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
    # fig = test(satellite)
    # output = io.BytesIO()
    # FigureCanvas(fig).print_png(output)
    # return Response(output.getvalue(), mimetype='image/png')
    return content
    


# Route API pour l'administrateur

# @app.route('/admin')


if __name__ == '__main__':
    app.run()