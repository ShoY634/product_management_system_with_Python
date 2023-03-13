from __future__ import annotations
from models.product import Product
from fixtures.product_data import pc, mouse

class Calculator:
    # purchase_list = [{"product": pc, "quantity": 1}, {"product": mouse, "quantity": 2}]
    # stock_add_list = [{'product': pc, 'quantity_add': 2}, {"product": mouse, "quantity_add": 1}]
    
    @classmethod
    def purchase_product(cls, purchase_list):
        for purchase in purchase_list:
            product_purchased = purchase["product"]
            product_purchased_quantity = purchase["quantity"]
            product_purchased_price = int(product_purchased_quantity * product_purchased.price * 1.1)
        
            print(f"商品「{product_purchased.name}」を{str(product_purchased_quantity)}個購入しました。")
            print(f"料金は{product_purchased_price}円です。")
            
            product_purchased.stock = product_purchased.stock - product_purchased_quantity
        
        
    @classmethod
    def add_stock(cls, stock_add_list):
        for adding in stock_add_list:
            product_add = adding['product']
            product_add_quantity = adding['quantity_add']
            
            print(f'商品{product_add.name}（在庫{product_add.stock}個）の在庫を{product_add_quantity}個追加しました。')
            product_add.stock = product_add.stock + product_add_quantity
            
            print(f'現在の在庫は{product_add.stock}個です。')
            