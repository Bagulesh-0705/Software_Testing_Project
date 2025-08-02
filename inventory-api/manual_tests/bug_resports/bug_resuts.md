# Bug Report – Manual Testing (Inventory API)
Tool Used: Postman  
Base URL: http://127.0.0.1:5000

---

## Summary

| Bug ID | Title                              | Status   | Severity | Area                  |
|--------|------------------------------------|----------|----------|-----------------------|
| BUG01  | Stock update allowed twice/day     | Open     | High     | PUT /products/<id>    |
| BUG02  | Electronics allowed price < 10     | Fixed    | High     | POST /products        |
| BUG03  | Category accepts invalid values    | Open     | Medium   | POST /products        |
| BUG04  | Missing name accepted              | Open     | High     | POST /products        |
| BUG05  | Non-existent product returns 200   | Fixed    | High     | GET /products/<id>    |
| BUG06  | Delete then fetch doesn't 404      | Fixed    | High     | DELETE /products/<id> |

---

## BUG01 – Stock Updated Twice in One Day

- **Steps to Reproduce:**
  1. POST a valid product
  2. PUT `/products/1` with `"stock": 12` → 200 OK
  3. PUT `/products/1` again on same day → 200 OK (should be 400)

- **Expected:** Second stock update should return 400 Bad Request
- **Actual:** Returns 200 OK and updates stock again
- **Severity:** HIGH
- **Suggested Fix:** Enforce date check using `datetime.utcnow().date()` per product ID

---

## BUG02 – Electronics Allowed with Price Below 10

- **Steps to Reproduce:**
  1. POST `/products` with:
     json
     {
       "name": "USB Cable",
       "category": "electronics",
       "price": 5.0,
       "stock": 10
     }
    

- **Expected:** 400 Bad Request (Electronics must have price ≥ 10)
- **Actual:** Product created with 201
- **Status:** FIXED (after validating price logic)
- **Severity:** HIGH

---

## BUG03 – Invalid Category Accepted

- **Steps to Reproduce:**
  1. POST product with `"category": "food"`

- **Expected:** 400 Bad Request (Invalid category)
- **Actual:** Product accepted
- **Severity:** MEDIUM
- **Fix Suggestion:** Use list validation `["electronics", "books", "clothing"]`

---

## BUG04 – Product Created Without Name

- **Steps to Reproduce:**
  1. POST product without `"name"` field

- **Expected:** 400 Bad Request
- **Actual:** Product created (ID generated, fields missing)
- **Severity:** HIGH
- **Fix Suggestion:** Add `if not name:` check

---

## BUG05 – GET Returns 200 for Non-existent Product

- **Steps to Reproduce:**
  1. GET `/products/9999`

- **Expected:** 404 Not Found
- **Actual:** 200 OK with empty object `{}` (before fix)
- **Status:** FIXED
- **Severity:** HIGH

---

## BUG06 – Deleted Product Still Returns 200

- **Steps to Reproduce:**
  1. DELETE `/products/1`
  2. GET `/products/1`

- **Expected:** 404 Not Found
- **Actual:** 200 OK (before fix)
- **Status:** FIXED
- **Severity:** HIGH

---

## Notes

- Manual testing revealed that most issues are around **missing field validation** and **business rules enforcement**.
- Recommended to add schema validation or helper validation functions for future improvements.