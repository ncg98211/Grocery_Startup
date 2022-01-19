from flask import Flask
from flask_restful import Api, reqparse
from dateutil import parser
from models import db, User, Grocery_List_DB, Grocery_Items_DB
from flask_cors import CORS

# Creating app
app = Flask(__name__)
api = Api(app)
CORS(app)

# Configuring database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Grocery_Startup.db'
app.config['BUNDLE_ERRORS'] = True
db.init_app(app)

# Creating database tables
with app.app_context():
    db.create_all()

# Arguments for grocery list
grocery_list_args = reqparse.RequestParser()
grocery_list_args.add_argument('grocery_list_description', type=str)
grocery_list_args.add_argument('delivery_datetime', type=str,
                               help="Please remember to add both a date and time you would like the item(s) to be delivered!")

# Arguments for grocery items
grocery_items_args = reqparse.RequestParser()
grocery_items_args.add_argument('item_id', type=str,
                                help="You need to specify an item id!")
grocery_items_args.add_argument('item_name', type=str,
                                help="Please remember to add the at least one grocery item!")

# Arguments for user data
user_args = reqparse.RequestParser()
user_args.add_argument('username', type=str, help="Please remember to add your username!")
user_args.add_argument('email', type=str, help="Please remember to add your email!")
user_args.add_argument('phone', type=str, help="Please remember to add your phone number!")
user_args.add_argument('delivery_address', type=str, help="Please remember to add your delivery address")


# Function that checks if the time and date entered by the user is a business day between 10am and 7pm
def check_DateTime(dateTimeString):
    if dateTimeString.weekday() < 5 and 10 <= dateTimeString.hour < 19:
        return True
    else:
        return False


# Gets user data. Since there is only one user for this app the function calls for an id equal to 1
@app.route("/api/user/", methods=['GET'])
def get_UserData():
    userData = User.query.filter_by(id=1).first()
    if userData:
        return userData.serialize
    else:
        # no user data in database
        return {
                   'error': 'There is no data for this user! Please add your information!'}, 404


# Updates or adds users to database
@app.route("/api/user/", methods=['PUT'])
def update_UserData():
    try:
        userData = user_args.parse_args()
        Selected_User = User.query.filter_by(id=1).first()

        if Selected_User:
            Selected_User.username = userData['username']
            Selected_User.email = userData['email']
            Selected_User.phone = userData['phone']
            Selected_User.delivery_address = userData['delivery_address']
            db.session.commit()
        else:
            # adding new user to database after detecting that user doesn't exist
            newUser = User(username=userData['username'],
                           email=userData['email'],
                           phone=userData['phone'],
                           delivery_address=userData['delivery_address'])

            db.session.add(newUser)
            db.session.commit()
        return {
            'message': 'User data has been successfully updated!'}, 200
    except:
        return {
            'error': 'Bad request. You must include all parameters!'}, 400


# Gets all grocery lists
@app.route("/api/grocery_list/", methods=["GET"])
def get_grocery_list():
    All_Grocery_Lists = Grocery_List_DB.query.all()
    if All_Grocery_Lists:
        return_dict = {}
        for Grocery_List in All_Grocery_Lists:
            return_dict[Grocery_List.grocery_list_id] = Grocery_List.serialize
        return return_dict
    else:
        return {
            'message': 'No grocery lists available! Start by creating your first one!'}, 404


# Creates a grocery list
@app.route("/api/grocery_list/", methods=["POST"])
def add_grocery_list():
    args = grocery_list_args.parse_args()
    try:
        dateTimeString = parser.isoparse(args['delivery_datetime'])
    except:
        return {
            'error': 'Invalid datetime string. Please make sure to follow the ISO 8601 format.'}, 404

    if check_DateTime(dateTimeString):
        newGroceryList = Grocery_List_DB(grocery_list_description=args['grocery_list_description'],
                                         delivery_datetime=args['delivery_datetime'])
        db.session.add(newGroceryList)
        db.session.commit()
        return {
            'message': 'Grocery list created successfully!'}, 200
    else:
        return {
            'error': 'Sorry, we only deliver on business days between the hours of 10AM to 7PM!'}, 404


# Deletes a grocery list specified by the user
@app.route("/api/grocery_list/delete/<grocery_list_id>", methods=["GET"])
def delete_grocery_list(grocery_list_id):
    if grocery_list_id:
        selected_list = Grocery_List_DB.query.filter_by(grocery_list_id=grocery_list_id)
        if selected_list:
            selected_list.delete()
            Grocery_Items_DB.query.filter_by(grocery_list_id=grocery_list_id).delete()
            db.session.commit()
            return {
                'message': 'Grocery list deleted successfully!'}, 200
        else:
            return {
                'error': 'Grocery list does not exist!'}, 404
    else:
        return {
            'error': 'You must specify a grocery list id to delete it!'}, 404


# Gets all items from all lists or all items from specific list
@app.route("/api/grocery_items/<grocery_list_id>", methods=["GET"])
@app.route("/api/grocery_items/", methods=["GET"])
def get_grocery_items(grocery_list_id=None):
    if grocery_list_id:
        grocery_items = Grocery_Items_DB.query.filter_by(grocery_list_id=grocery_list_id).all()
    else:
        grocery_items = Grocery_Items_DB.query.all()

    if grocery_items:
        item_list = []
        return_dict = {}
        for grocery_item in grocery_items:
            item_list.append(grocery_item.serialize)
        return_dict[grocery_list_id] = item_list
        return return_dict
    else:
        return {
            'message': 'No items to show. Try adding some to begin!'}, 404


# Adds a grocery item to a specific list
@app.route("/api/grocery_items/<grocery_list_id>", methods=["POST"])
def add_grocery_item(grocery_list_id):
    args = grocery_items_args.parse_args()
    grocery_item = args['item_name']
    item_id = args['item_id']
    if grocery_item:
        newGroceryItem = Grocery_Items_DB(item_name=grocery_item, item_id=item_id, grocery_list_id=grocery_list_id)
        db.session.add(newGroceryItem)
        db.session.commit()
        return {
            'message': 'Item added successfully!'}, 200
    else:
        return {
            'error': 'No item was specified'}, 404


# Deletes specified grocery item
@app.route("/api/grocery_items/delete/<grocery_item_id>", methods=["GET"])
def delete_grocery_item(grocery_item_id):
    if grocery_item_id:
        selected_item = Grocery_Items_DB.query.filter_by(item_id=grocery_item_id)
        if selected_item:
            selected_item.delete()
            db.session.commit()
            return {
                'message': 'Grocery item deleted successfully!'}, 200
        else:
            return {
                'error': 'Grocery item does not exist!'}, 404
    else:
        return {
            'error': 'You must specify a grocery item id to delete it!'}, 404


if __name__ == "__main__":
    app.run(debug=True)
