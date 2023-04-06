from sat_libraries import user, admin
from flask import Flask, jsonify

app = Flask(__name__)

## Routes :

# Route API pour l'utilisateur
@app.route('/user')
def show_user_interface():
    return user.get_all_satellite_data()


# Route API pour l'administrateur

# @app.route('/admin')


if __name__ == '__main__':
    app.run()