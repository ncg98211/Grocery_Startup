from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Creates database table which defines user scheme
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    delivery_address = db.Column(db.String(50), nullable=False)

    def __init__(self, username, email, phone, delivery_address):
        self.username = username
        self.email = email
        self.phone = phone
        self.delivery_address = delivery_address

    @property
    def serialize(self):

        return {
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'delivery_address': self.delivery_address
        }


# Creates database table which defines grocery list scheme
class Grocery_List_DB(db.Model):
    grocery_list_id = db.Column(db.Integer, primary_key=True)
    grocery_list_description = db.Column(db.String(50), nullable=True)
    delivery_datetime = db.Column(db.String(50), nullable=False)

    def __init__(self, grocery_list_description, delivery_datetime):
        self.grocery_list_description = grocery_list_description
        self.delivery_datetime = delivery_datetime

    @property
    def serialize(self):
        return {
            'grocery_list_description': self.grocery_list_description,
            'delivery_datetime': self.delivery_datetime
        }


# Creates database table which defines grocery item scheme
class Grocery_Items_DB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String(100))
    grocery_list_id = db.Column(db.Integer, nullable=False)
    item_name = db.Column(db.String(50), nullable=False)

    def __init__(self, item_id, item_name, grocery_list_id):
        self.item_id = item_id
        self.item_name = item_name
        self.grocery_list_id = grocery_list_id

    @property
    def serialize(self):

        return {
            'id': self.item_id,
            'item_name': self.item_name
        }

