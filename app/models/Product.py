""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
   

    def model_add_product(self, product_info):
        query = "INSERT INTO products (name, description, Price, created_at) VALUES (:name, :description, :price, NOW())"
        data = {
            'name': product_info['Name'],
            'description': product_info['Description'],
            'price': product_info['Price']
        }
        self.db.query_db(query, data)

    def get_all_products(self):
        query = "SELECT * FROM products"
        list_of_product = self.db.query_db(query)
        return list_of_product

    def display_products(self, id):
        query = "SELECT * FROM products WHERE id = :id"
        data = {
            'id': id 
        }
        display = self.db.query_db(query, data)
        return display

    def edit_products(self, product_update, id):
        query = "UPDATE products SET name=:name, description=:description, price =:price WHERE id = :id"
        data = {
            'name':product_update['Updated_Name'],
            'description': product_update['Updated_Description'],
            'price': product_update['Updated_Price'],
            'id': id
        }

        model_update = self.db.query_db(query, data)
        return model_update

    def model_delete(self, id):
        query = "DELETE FROM products WHERE id = :id "
        data = {
            'id': id
        }
        yes = self.db.query_db(query, data)
        return yes












