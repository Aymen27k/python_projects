import random
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

load_dotenv()
API_SECRET_KEY = os.getenv("API-KEY")

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "map_url": self.map_url,
        "img_url": self.img_url,
        "location": self.location,
        "seats": self.seats,
        "has_toilet": self.has_toilet,
        "has_wifi": self.has_wifi,
        "has_sockets": self.has_sockets,
        "can_take_calls": self.can_take_calls,
        "coffee_price": self.coffee_price
    }


@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random")
def random_cafe():
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


## HTTP GET - Read Record
@app.get("/all")
def all_cafes():
    all_cafes = Cafe.query.all()
    cafe_container = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafe_container)

@app.get("/search")
def search_cafes():

    location = request.args.get("loc")
    cafe_found = Cafe.query.filter_by(location=location).all()
    if cafe_found:
        result = [cafe.to_dict() for cafe in cafe_found]
        return jsonify(cafes=result)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


    
## HTTP POST - Create Record
def str_to_bool(value):
    return value.lower() == "true"


@app.post("/add")
def add_cafe():
    name = request.form.get("name")
    location = request.form.get("location")
    map_url = request.form.get("map_url")
    img_url = request.form.get("img_url")
    has_sockets = str_to_bool(request.form.get("has_sockets"))
    has_toilet = str_to_bool(request.form.get("has_toilet"))
    has_wifi = str_to_bool(request.form.get("has_wifi"))
    can_take_calls = str_to_bool(request.form.get("can_take_calls"))
    seats = request.form.get("seats")
    coffee_price = request.form.get("coffee_price")
    
    new_cafe = Cafe(
        name=name,
        location=location,
        map_url=map_url,
        img_url=img_url,
        has_sockets=has_sockets,
        has_toilet =has_toilet,
        has_wifi=has_wifi,
        can_take_calls=can_take_calls,
        seats=seats,
        coffee_price=coffee_price
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify({
    "status": "success",
    "cafe": {
        "id": new_cafe.id,
        "name": new_cafe.name,
        "location": new_cafe.location,
        "coffee_price": new_cafe.coffee_price
    }
}), 201




## HTTP PUT/PATCH - Update Record

@app.patch("/update-price/<int:cafe_id>")
def change_price(cafe_id):
    cafe_found = db.session.get(Cafe, cafe_id)
    if not cafe_found:
        return jsonify({
        "error": {
            "Not Found": "Sorry a cafe with that ID was not found in the Database"
        }
    }), 404
    new_price = request.args.get("new_price")
    if not new_price:
        return jsonify({
        "status": "error",
        "message": "Missing or empty coffee price"
    }), 400
    cafe_found.coffee_price = new_price
    db.session.commit()


    return jsonify({
        "status": "success",
        "message": f"Updated coffee price to {new_price} for café ID {cafe_id}"
    }), 200
## HTTP DELETE - Delete Record

@app.delete("/report-closed/<cafe_id>")
def delete_cafe(cafe_id):
    cafe_found = db.session.get(Cafe, cafe_id)
    if not cafe_found:
        return jsonify({
        "error": {
            "Not Found": "Sorry a cafe with that ID was not found in the Database"
        }
    }), 404
    api_key = request.args.get("api-key")
    if api_key != API_SECRET_KEY:
        return jsonify({
            "error": "Unauthorized. Invalid API key."
        }), 403
    
    db.session.delete(cafe_found)
    db.session.commit()
    return jsonify({
    "success": "Café deleted successfully."
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
