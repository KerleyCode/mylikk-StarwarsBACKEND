from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_character_favorites = db.Table('user_character_favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'), primary_key=True)
)

user_planet_favorites = db.Table('user_planet_favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('planet_id', db.Integer, db.ForeignKey('planet.id'), primary_key=True)
)

user_starship_favorites = db.Table('user_starship_favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('starship_id', db.Integer, db.ForeignKey('starships.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    favorite_characters = db.relationship('Character', secondary=user_character_favorites, backref=db.backref('favorited_by', lazy='dynamic'))
    favorite_planets = db.relationship('Planet', secondary=user_planet_favorites, backref=db.backref('favorited_by', lazy='dynamic'))
    favorite_starships = db.relationship('Starships', secondary=user_starship_favorites, backref=db.backref('favorited_by', lazy='dynamic'))

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favorite_characters": [char.id for char in self.favorite_characters],
            "favorite_planets": [planet.id for planet in self.favorite_planets],
            "favorite_starships": [starship.id for starship in self.favorite_starships],
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    hair_color = db.Column(db.String(120), unique=False, nullable=False)
    skin_color = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    orbital_period = db.Column(db.Integer, unique=False, nullable=False)
    rotation_period = db.Column(db.Integer, unique=False, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
        }

class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(120), unique=False, nullable=False)
    starship_class = db.Column(db.String(120), unique=False, nullable=False)
    manufacturer = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Starships %r>' % self.model

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
        }
