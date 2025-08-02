from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)
products = {}
stock_update_dates = {}
inventory={}
last_updated={}
current_id = 1

def validate_product(data, is_update=False, existing_product=None):
    errors = []

    if not is_update or "name" in data:
        name = data.get("name", "").strip()
        if not name:
            errors.append("Name is required and cannot be empty.")
        elif len(name) > 100:
            errors.append("Name must not exceed 100 characters.")

    if not is_update or "category" in data:
        category = data.get("category")
        if category not in ["electronics", "books", "clothing"]:
            errors.append("Category must be one of: electronics, books, clothing.")

    if not is_update or "price" in data:
        try:
            price = float(data.get("price", 0))
            if price < 0:
                errors.append("Price must be ≥ 0.")
            effective_category = data.get("category") or (existing_product or {}).get("category")
            if effective_category == "electronics" and price < 10:
                errors.append("Price must be ≥ 10 for electronics.")
        except (ValueError, TypeError):
            errors.append("Price must be a number.")

    if not is_update or "stock" in data:
        try:
            stock = int(data.get("stock", 0))
            if stock < 0:
                errors.append("Stock must be ≥ 0.")
        except (ValueError, TypeError):
            errors.append("Stock must be an integer.")

    return errors

@app.route('/products', methods=['GET'])
def list_products():
    return jsonify(list(products.values())), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

@app.route('/products/<int:product_id>/stock', methods=['PATCH'])
def update_stock(product_id):
    today = datetime.today().date()

    if product_id not in inventory:
        return jsonify({"error": "Product not found"}), 404

    if last_updated.get(product_id) == today:
        return jsonify({"error": "Stock can only be updated once per day"}), 400

    data = request.get_json()
    if "stock" not in data or not isinstance(data["stock"], int) or data["stock"] < 0:
        return jsonify({"error": "Invalid stock value"}), 400

    inventory[product_id]["stock"] = data["stock"]
    last_updated[product_id] = today

    return jsonify({"message": "Stock updated"}), 200

@app.route('/products', methods=['POST'])
def create_product():
    global current_id

    data = request.get_json()
    errors = validate_product(data)
    if errors:
        return jsonify({"errors": errors}), 400

    product = {
        "id": current_id,
        "name": data["name"],
        "category": data["category"],
        "price": data["price"],
        "stock": data["stock"]
    }

    products[current_id] = product
    stock_update_dates[current_id] = datetime.utcnow().date()
    current_id += 1

    return jsonify(product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = products.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    errors = validate_product(data, is_update=True, existing_product=product)
    if errors:
        return jsonify({"errors": errors}), 400


    if "stock" in data:
        today = datetime.utcnow().date()
        last_update = stock_update_dates.get(product_id)

        if last_update == today:
            return jsonify({"error": "Stock can only be updated once per day"}), 400
        stock_update_dates[product_id] = today

    for key in data:
        product[key] = data[key]

    return jsonify(product), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = products.pop(product_id, None)
    stock_update_dates.pop(product_id, None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"message": "Product deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)