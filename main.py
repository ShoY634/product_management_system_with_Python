from fixtures.product_data import pc
from helper.product_calculator import Calculator


a = Calculator.purchase_product(purchase_list = [{"product": pc, "quantity": 1}])