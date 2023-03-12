from fixtures.product_data import pc, mouse
from helper.product_calculator import Calculator


a = Calculator.purchase_product(purchase_list = [{"product": pc, "quantity": 1}, {"product": mouse, "quantity": 2}])
b = Calculator.add_stock(stock_add_list = [{'product': pc, 'quantity_add': 2}, {"product": mouse, "quantity_add": 1}])