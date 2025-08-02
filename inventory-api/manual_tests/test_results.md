# Manual Test Results - Inventory Management API

| Test Case                                  | Expected Result           | Actual Result     | Status |
|--------------------------------------------|----------------------------|--------------------|--------|
| GET /products (empty)                      | Return empty list          | Pass               | ✅     |
| POST valid product                         | Product created (201)      | Pass               | ✅     |
| POST invalid (empty name)                  | 400 with error message     | Pass               | ✅     |
| POST invalid (bad category)                | 400 with error message     | Pass               | ✅     |
| POST invalid (price < 0)                   | 400 with error             | Pass               | ✅     |
| POST electronics with price < 10           | 400 with message           | Pass               | ✅     |
| PUT /products/{id} update price only       | 200 with updated product   | Pass               | ✅     |
| PUT stock update once/day valid            | 200 success                | Pass               | ✅     |
| PUT stock update again same day            | 400 with message           | Pass               | ✅     |
| GET /products/{invalid_id}                 | 404 Not Found              | Pass               | ✅     |
| DELETE valid ID                            | 200 success or 204         | Pass               | ✅     |
| DELETE already-deleted product             | 404 Not Found              | Pass               | ✅     |