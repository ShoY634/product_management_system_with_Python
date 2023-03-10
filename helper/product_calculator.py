from __future__ import annotations
from models.product import Product
from fixtures.product_data import pc

class Calculator:
    purchase_list = [{"product": pc, "quantity": 1}]
    
    @classmethod
    def purchase_product(cls, purchase_list):
        # ここらへん後で最適化したい。てかprintの中身がfstringsで書くとばぐって困る。なんで？
        product_purchased = purchase_list[0]["product"]
        product_purchased_quantity = purchase_list[0]["quantity"]
        product_purchased_price = int(product_purchased_quantity * product_purchased.price * 1.1)

        print(f"商品「{product_purchased.name}」を{str(product_purchased_quantity)}個購入しました。")
        
        pc.stock -= purchase_list[0]["quantity"]
        
        print(f"料金は{product_purchased_price}円です。")
        