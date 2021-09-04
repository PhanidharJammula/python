from flask import Flask, request
import json

app = Flask(__name__)

product_price = {"CH1":3.11, "AP1":6.00, "CF1":11.23, "MK1":4.75, "OM1":3.69}

offers = {"BOGO": }

@app.route('/calculate', methods=['GET', 'POST'])
def calculate_bill():

    basket_list = request.args.get("basket")
    basket_list = json.loads(basket_list)
    total = 0.0
    print(basket_list, type(basket_list))

    for product in basket_list:
        print(product)

        if product not in product_price:
            print("product %s not in list"%(product))
            raise "Invalid Product name"

        total += product_price[product]

    print(total)

    return "first is working"

if __name__ == "__main__":
    app.run(host="localhost", port=5050, debug=True)
