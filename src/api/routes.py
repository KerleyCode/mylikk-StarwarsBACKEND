from flask import Blueprint, request, jsonify
from api.models import db, User, Character, Planet, Starships
from api.utils import APIException
from flask_cors import CORS

api = Blueprint('api', __name__)
CORS(api)

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200

@api.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(email=data['email'], password=data['password'], is_active=True)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 201

@api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200

@api.route('/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    return jsonify([character.serialize() for character in characters]), 200

@api.route('/characters', methods=['POST'])
def create_character():
    data = request.json
    new_character = Character(**data)
    db.session.add(new_character)
    db.session.commit()
    return jsonify(new_character.serialize()), 201

@api.route('/characters/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    character = Character.query.get(character_id)
    if character is None:
        raise APIException('Character not found', status_code=404)
    db.session.delete(character)
    db.session.commit()
    return jsonify({"message": "Character deleted"}), 200

@api.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    return jsonify([planet.serialize() for planet in planets]), 200

@api.route('/planets', methods=['POST'])
def create_planet():
    data = request.json
    new_planet = Planet(**data)
    db.session.add(new_planet)
    db.session.commit()
    return jsonify(new_planet.serialize()), 201

@api.route('/planets/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        raise APIException('Planet not found', status_code=404)
    db.session.delete(planet)
    db.session.commit()
    return jsonify({"message": "Planet deleted"}), 200

@api.route('/starships', methods=['GET'])
def get_starships():
    starships = Starships.query.all()
    return jsonify([starship.serialize() for starship in starships]), 200

@api.route('/starships', methods=['POST'])
def create_starship():
    data = request.json
    new_starship = Starships(**data)
    db.session.add(new_starship)
    db.session.commit()
    return jsonify(new_starship.serialize()), 201

@api.route('/starships/<int:starship_id>', methods=['DELETE'])
def delete_starship(starship_id):
    starship = Starships.query.get(starship_id)
    if starship is None:
        raise APIException('Starship not found', status_code=404)
    db.session.delete(starship)
    db.session.commit()
    return jsonify({"message": "Starship deleted"}), 200

@api.route('/users/<int:user_id>/favorites/<string:favorite_type>/<int:favorite_id>', methods=['POST'])
def add_favorite(user_id, favorite_type, favorite_id):
    user = User.query.get(user_id)
    if user is None:
        raise APIException('User not found', status_code=404)

    if favorite_type == 'character':
        favorite = Character.query.get(favorite_id)
        if favorite is None:
            raise APIException('Character not found', status_code=404)
        user.favorite_characters.append(favorite)
    elif favorite_type == 'planet':
        favorite = Planet.query.get(favorite_id)
        if favorite is None:
            raise APIException('Planet not found', status_code=404)
        user.favorite_planets.append(favorite)
    elif favorite_type == 'starship':
        favorite = Starships.query.get(favorite_id)
        if favorite is None:
            raise APIException('Starship not found', status_code=404)
        user.favorite_starships.append(favorite)
    else:
        raise APIException('Invalid favorite type', status_code=400)

    db.session.commit()
    return jsonify(user.serialize()), 200

@api.route('/users/<int:user_id>/favorites/<string:favorite_type>/<int:favorite_id>', methods=['DELETE'])
def remove_favorite(user_id, favorite_type, favorite_id):
    user = User.query.get(user_id)
    if user is None:
        raise APIException('User not found', status_code=404)

    if favorite_type == 'character':
        favorite = Character.query.get(favorite_id)
        if favorite is None:
            raise APIException('Character not found', status_code=404)
        user.favorite_characters.remove(favorite)
    elif favorite_type == 'planet':
        favorite = Planet.query.get(favorite_id)
        if favorite is None:
            raise APIException('Planet not found', status_code=404)
        user.favorite_planets.remove(favorite)
    elif favorite_type == 'starship':
        favorite = Starships.query.get(favorite_id)
        if favorite is None:
            raise APIException('Starship not found', status_code=404)
        user.favorite_starships.remove(favorite)
    else:
        raise APIException('Invalid favorite type', status_code=400)

    db.session.commit()
    return jsonify(user.serialize()), 200
