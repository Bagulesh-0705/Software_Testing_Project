import requests
from datetime import datetime

BASE_URL = "http://localhost:5000"

# Helper to create a valid product
def create_product(name="Laptop", category="electronics", price=1200.0, stock=10):
    payload = {
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }
    res = requests.post(f"{BASE_URL}/products", json=payload)
    return res

# Test creating a valid product
def test_create_product_valid():
    res = create_product()
    assert res.status_code == 201
    data = res.json()
    assert data["name"] == "Laptop"
    assert data["category"] == "electronics"
    assert data["price"] == 1200.0
    assert data["stock"] == 10

# Test creating product with invalid name
def test_create_product_invalid_name():
    res = create_product(name="")
    assert res.status_code == 400

# Test invalid category
def test_create_product_invalid_category():
    res = create_product(category="furniture")
    assert res.status_code == 400

# Test electronics with price less than 10
def test_create_product_invalid_electronics_price():
    res = create_product(price=5.0)
    assert res.status_code == 400

# Test get all products
def test_get_all_products():
    res = requests.get(f"{BASE_URL}/products")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

# Test get product by ID
def test_get_single_product():
    new_res = create_product(name="Mouse", price=15.0)
    pid = new_res.json()["id"]
    res = requests.get(f"{BASE_URL}/products/{pid}")
    assert res.status_code == 200
    assert res.json()["name"] == "Mouse"

# Test get non-existent product
def test_get_product_not_found():
    res = requests.get(f"{BASE_URL}/products/9999")
    assert res.status_code == 404

# Test update product details
def test_update_product_name():
    new_res = create_product(name="Tablet", price=100.0)
    pid = new_res.json()["id"]
    res = requests.put(f"{BASE_URL}/products/{pid}", json={"name": "iTablet"})
    assert res.status_code == 200
    assert res.json()["name"] == "iTablet"

# Test update stock twice on same day (should fail)
def test_update_stock_once_per_day():
    new_res = create_product(name="TV", price=500.0, stock=5)
    pid = new_res.json()["id"]
    # First stock update
    res1 = requests.put(f"{BASE_URL}/products/{pid}", json={"stock": 15})
    assert res1.status_code == 200
    # Second update on same day
    res2 = requests.put(f"{BASE_URL}/products/{pid}", json={"stock": 20})
    assert res2.status_code == 400
    assert "Stock can only be updated once" in res2.json()["error"]

# Test delete product
def test_delete_product():
    new_res = create_product(name="ToDelete", price=20.0)
    pid = new_res.json()["id"]
    res = requests.delete(f"{BASE_URL}/products/{pid}")
    assert res.status_code == 204
    # Ensure it's gone
    res_check = requests.get(f"{BASE_URL}/products/{pid}")
    assert res_check.status_code == 404                                             