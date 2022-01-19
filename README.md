# Grocery Startup 
## _A RESTful API with Flask, React, & SQLAlchemy_
---
Coding project for Armada Power coding assessment. Even if I'm not selected for the role I would love feedback!
## Installation
I used the version **Python 3.9.0** for development.

To install dependencies navigate to the **flask_backend** and run:
```sh
pip install -r requirements.txt
```
Then navigate to the **react_frontend** folder & run (make sure you have npm installed first):
```sh
npm install
```


## How to run
Start by navigating to the **flask_backend** folder & run the main.py file:
```sh
python main.py
```
Next navigate to the **react_frontend** folder & run following command:
```sh
npm start 
```

Finally, navigate to the following address in your browser for the React Front-end:
```sh
127.0.0.1:3000
```
---
# API Documentation
---
## Get User
Grabs user data from the table. Since the user is already authenticated. It only grabs the data of one user!


- ####  URL
    /api/user/
- ####  Method
    `GET`
- #### URL Params
    None
- #### Data Params
    None
- #### Success Response
  - Code: **200**
  - Content: 
    ```
    {"username": "Bobby Tables",
     "email": "Bob.Tables@gmail.com", 
     "phone": "(716) 867-5309", 
     "delivery_address": "890 Fifth Avenue, Manhattan, New York City"}
    ```
- #### Error Response
  - Code: **404**
  - Content: `{"error": "There is no data for this user! Please add your information!"}`
---
## Update/Add User
Update or adds user data to database. Since the user is already authenticated. It only updates/adds the data with the user id equal to 1!

- ####  URL
    /api/user/
- ####  Method
    `PUT`
- #### URL Params
    None
- #### Data Params
    ```
    data = {"username": "Bobby Tables",
            "email": "Bob.Tables@gmail.com", 
            "phone": "(716) 867-5309", 
            "delivery_address": "890 Fifth Avenue, Manhattan, New York City"}
    ```
- #### Success Response
  - Code: **200**
  - Content: 
    ```
    {'message': 'User data has been successfully updated!'}
    ```
- #### Error Response
  - Code: **400**
  - Content: `{'error': 'Bad request. You must include all parameters!'}`
---
## Get All Grocery Lists
Gets all grocery lists.

- ####  URL
    /api/grocery_list/
- ####  Method
    `GET`
- #### URL Params
    None
- #### Data Params
    None
- #### Success Response
  - Code: **200**
  - Content: 
    ```
    {
      "1": {
        "delivery_datetime": "2022-01-10T17:26:05+0000", 
        "grocery_list_description": "Buffalo Wing Dip"
      }
    }
    ```
- #### Error Response
  - Code: **404**
  - Content:
    ```
    {'message': 'No grocery lists available! Start by creating your first one!'}
    ```
---
## Create a Grocery List
Allows user to create a grocery list.


- ####  URL
    /api/grocery_list/
- ####  Method
    `POST`
- #### URL Params
    None
- #### Data Params
    ```
    data={"grocery_list_description": "Normal Grocery List",
          "delivery_datetime": "2022-01-10T17:26:05+0000"}
    ```
- #### Success Response
  - Code: **200**
  - Content: 
    ```
    {'message': 'Grocery list created successfully!'}
    ```
- #### Error Response(s)
  - Code: **404**
  - Content: 
       ```
       {'error': 'Invalid datetime string. Please make sure to follow the ISO 8601 format.'}
       ```
       ```
       {'error': 'Sorry, we only deliver on business days between the hours of 10AM to 7PM!'}
       ```
---
## Delete Grocery List
Deletes a grocery list and all items within that list.

- ####  URL
    /api/grocery_list/delete/<grocery_list_id>
- ####  Method
    `GET`
- #### URL Params
    `grocery_list_id=[integer]`
- #### Data Params
    None
- #### Success Response
  - Code: **200**
  - Content: 
    ```
    {'message': 'Grocery list deleted successfully!'}
    ```
- #### Error Response
  - Code: **404**
  - Content: 
    ```
    {'error': 'Grocery list does not exist!'}
    ```
    ```
    {'error': 'You must specify a grocery list id to delete it!'}
    ```
---    
## Get Grocery Items
Grabs all grocery item(s) from all lists or all grocery item(s) from one list.
- ####  URL(s)
    - /api/grocery_items/<grocery_list_id>
    - /api/grocery_items/
- ####  Method
    `GET`
- #### URL Params
    None
- #### Data Params
     Optional: `grocery_list_id=[integer]`
- #### Success Response
  - Code: **200**
  - Content: 
    ```
        {
      "1": [
            {
              "id": "a389b1a8-764d-471c-8a64-8aafd39c6547", 
              "item_name": "Milk"
            }, 
            {
              "id": "645a5728-9acb-4014-84d9-ec6d9bfa7b2a", 
              "item_name": "Bread"
            }
           ]
         }
    ```
- #### Error Response
  - Code: **404**
  - Content: 
    ```
    {'message': 'No items to show. Try adding some to begin!'}
    ```
---
## Adds a Grocery Item
Adds a grocery item to a specific list.

- ####  URL
    /api/grocery_items/<grocery_list_id>
- ####  Method
    `POST`
- #### URL Params
    `grocery_list_id=[grocery_list_id]`
- #### Data Params
    ```
    data = {'grocery_item': 'Milk'}
    ```
- #### Success Response
  - Code: **200**
  - Content: 
    ```
    {'message': 'Item added successfully!'}
    ```
- #### Error Response
  - Code: **404**
  - Content:
    ```
    {'error': 'No item was specified'}
    ```
---
## Delete an Item from Grocery List
Deletes an item from a Grocery List.

- ####  URL
    /api/grocery_items/delete/<grocery_item_id>
- ####  Method
    `GET`
- #### URL Params
    `grocery_item_id=[integer]`
- #### Data Params
    None
- #### Success Response
  - Code: **200**
  - Content: 
    ```
    {'message': 'Grocery item deleted successfully!'}
    ```
- #### Error Response
  - Code: **404**
  - Content: 
    ```
    {'error': 'Grocery item does not exist!'}
    ```
    ```
    {'error': 'You must specify a grocery item id to delete it!'}
    ```

## License

MIT
