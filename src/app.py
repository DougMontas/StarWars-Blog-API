from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# db = SQLAlchemy()


# CHARACTER PAGE -----------------------------------------


@app.route('/character', methods=['GET'])
def get_character():
    json_text = jsonify(swapi_character)
    return json_text
    


swapi_character = [
    {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",  
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": "https://swapi.dev/api/planets/1/"
    }
]


@app.route('/character', methods=['POST'])
def post_character():
    payload = request.get_json(force=True)
    swapi_character.append(payload)
    return jsonify(swapi_character)


@app.route('/character/<int:position>', methods=['DELETE'])
def delete_character(position):
    swapi_character.pop(position)
    return jsonify(swapi_character)

# CHARACTER PAGE -----------------------------------------


# PLANETS PAGE -----------------------------------------


@app.route('/planets', methods=['GET'])
def get_planets():
    json_text = jsonify(swapi_planets)
    return json_text
    #   return '<h1>Hello</h1>'


swapi_planets = [
    {
        "name": "Tatooine",
        "rotation_period": "23",
        "orbital_period": "304",
        "diameter": "10465",
        "climate": "arid",
        "gravity": "1 standard",
        "terrain": "desert",
        "surface_water": "1",
        "population": "200000"
    }
]


@app.route('/planets', methods=['POST'])
def post_planets():
    payload = request.get_json(force=True)
    swapi_planets.append(payload)
    return jsonify(swapi_planets)


@app.route('/planets/<int:position>', methods=['DELETE'])
def delete_planets(position):
    swapi_planets.pop(position)
    return jsonify(swapi_planets)

# PLANETS PAGE -----------------------------------------

# SPECIES PAGE -----------------------------------------


@app.route('/species', methods=['GET'])
def get_species():
    json_text = jsonify(swapi_species)
    return json_text
    #   return '<h1>Hello</h1>'


swapi_species = [
    {
        "name": "Human",
        "classification": "mammal",
        "designation": "sentient",
        "average_height": "180",
        "skin_colors": "caucasian, black, asian, hispanic",
        "hair_colors": "blonde, brown, black, red",
        "eye_colors": "brown, blue, green, hazel, grey, amber",
        "average_lifespan": "120",
        "homeworld": "https://swapi.dev/api/planets/9/",
        "language": "Galactic Basic"
    }
]


@app.route('/species', methods=['POST'])
def post_species():
    payload = request.get_json(force=True)
    swapi_species.append(payload)
    return jsonify(swapi_species)


@app.route('/species/<int:position>', methods=['DELETE'])
def delete_species(position):
    swapi_species.pop(position)
    return jsonify(swapi_species)


# SPECIES PAGE -----------------------------------------


# VEHICLE PAGE -----------------------------------------

@app.route('/vehicle', methods=['GET'])
def get_vehicle():
    json_text = jsonify(swapi_vehicle)
    return json_text


swapi_vehicle = [
    {
        "name": "Sand Crawler",
        "model": "Digger Crawler",
        "manufacturer": "Corellia Mining Corporation",
        "cost_in_credits": "150000",
        "length": "36.8 ",
        "max_atmosphering_speed": "30",
        "crew": "46",
        "passengers": "30",
        "cargo_capacity": "50000",
        "consumables": "2 months",
        "vehicle_class": "wheeled",
        "pilots": [],
    }
]


@app.route('/vehicle', methods=['POST'])
def post_vehicle():
    payload = request.get_json(force=True)
    swapi_vehicle.append(payload)
    return jsonify(swapi_vehicle)


@app.route('/vehicle/<int:position>', methods=['DELETE'])
def delete_vehicle(position):
    swapi_vehicle.pop(position)
    return jsonify(swapi_vehicle)


# VEHICLE PAGE -----------------------------------------


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
