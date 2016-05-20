"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Product')
        self.db = self._app.db

   
    def index(self):
        product_list = self.models['Product'].get_all_products()
        return self.load_view('index.html', product_list = product_list)


    def add(self):
        return self.load_view('add.html')

    def control_add_product(self):
        product_info = {
            "Name": request.form['product_name'],
            "Description": request.form['product_description'],
            "Price": request.form['price']
        }

        self.models['Product'].model_add_product(product_info)
        return redirect('/')

    def show(self, id):
        show = self.models['Product'].display_products(id)
        return self.load_view('show.html', show = show[0])

    def edit(self, id):
        edit_show = self.models['Product'].display_products(id) 
        return self.load_view('edit.html', edit_show = edit_show[0])

    def update(self, id):
        product_update = {
            'Updated_Name': request.form['update_product_name'],
            'Updated_Description': request.form['update_product_description'],
            'Updated_Price': request.form['update_price']
            # 'id': id 
        }

        self.models['Product'].edit_products(product_update, id)
        return redirect ('/')

    def delete(self, id):
        delete_product = self.models['Product'].display_products(id)
        return self.load_view('delete.html', delete_product = delete_product[0])

    def erase(self, id):

        self.models['Product'].model_delete(id)
        return redirect ('/')















        