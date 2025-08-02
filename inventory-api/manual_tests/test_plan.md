# Manual Testing Test Plan - Inventory Management API

## Objective
To validate the functionality, correctness, and business rules of the Inventory Management API using manual tests in Postman.




## Endpoints Tested

| Method | Endpoint            | Purpose                                |
|--------|---------------------|----------------------------------------|
| GET    | /products           | List all products                      |
| GET    | /products/{id}      | Get product by ID                      |
| POST   | /products           | Create a new product                   |
| PUT    | /products/{id}      | Update product (price, stock, etc.)    |
| DELETE | /products/{id}      | Delete a product by ID                 |




## Business Rules Tested

| Rule   | Rule Description                                                                  |
|--------|-----------------------------------------------------------------------------------|
| 1      | `name` is required, non-empty, max 100 characters.                                |
| 2      | `category` must be one of: "electronics", "books", "clothing".                    |
| 3      | `price` must be ≥ 0; if category is "electronics", price must be ≥ 10.            |
| 4      | `stock` must be integer ≥ 0.                                                      |
| 5      | `stock` can only be updated once per calendar day per product.                    |
| 6      | Invalid or missing fields return HTTP 400 with proper error message.              |
| 7      | Non-existent product ID returns HTTP 404.                                         |




## Test Data Used

- Valid products (all fields correct)
- Invalid inputs (missing name, wrong category, price < 0, "electronics_price" < 10, etc.)
- Duplicate stock update in same day
- Random ID (99) for 404 test