# Software_Testing_Project
Halleyx-Software_Testing_Project
# Halleyx - Software Testing Challenge -  2025

## Overview

You will design, implement, and test a RESTful Inventory Management API with unique business rules. This is a full-stack QA + backend challenge:

- **Build the API** with specific validation and constraints.
- **Design, implement, and run automated tests** covering all aspects.
- Perform **exploratory/manual testing** to identify bugs or unexpected behaviors.
- Deliver **comprehensive documentation** including test plans, bug reports, and reflective summaries.

This challenge will assess your ability to code, test, and communicate professionally.

---

## Part 1: Build the Custom Inventory API

---

### Product Data Model

| Field | Type | Constraints & Business Rules |
| --- | --- | --- |
| `id` | Integer | Auto-generated unique identifier (starting at 1, incrementing) |
| `name` | String | Required, non-empty, max length 100 characters |
| `category` | String | Required, one of: `"electronics"`, `"books"`, `"clothing"` |
| `price` | Float | Must be ≥ 0; **if category = "electronics", price must be ≥ 10** |
| `stock` | Integer | Must be ≥ 0; stock can only be updated **once per product per calendar day** |

---

### API Endpoints

| Method | Endpoint | Request Body Example | Response Notes |
| --- | --- | --- | --- |
| GET | `/products` | None | Returns list of all products |
| GET | `/products/{id}` | None | Returns product details or 404 if not found |
| POST | `/products` | `{ "name": "Laptop", "category": "electronics", "price": 1200.50, "stock": 10 }` | Creates product; validates rules; returns created product with `id` |
| PUT | `/products/{id}` | Partial or full update; e.g., `{ "price": 1150, "stock": 12 }` | Updates product; enforces stock update rule; returns updated product or 404 if not found |
| DELETE | `/products/{id}` | None | Deletes product or 404 if not found |

---

### Business Rules to Enforce

1. `name` must be present, non-empty, and max 100 characters.
2. `category` must be exactly one of `"electronics"`, `"books"`, or `"clothing"`.
3. `price` must be a float ≥ 0. If `category` is `"electronics"`, then `price` must be ≥ 10.
4. `stock` must be an integer ≥ 0.
5. A product’s `stock` field **can only be updated once per calendar day**. Attempts to update `stock` more than once per day must return HTTP 400 with an explanatory error message.
6. All other invalid or missing fields must return HTTP 400 with clear error messages.
7. Requests referencing a non-existent `id` must return HTTP 404.

---

### Implementation Details

- Use any backend framework or language (Node.js, Python, Java, etc.).
- Store data **in-memory**; persistence is not required.
- API must respond in JSON with appropriate HTTP status codes.
- Implement error handling with clear JSON messages.
- For date tracking on stock updates, use server’s system date (assume UTC).
- Base URL is `http://localhost:5000` or equivalent.

---

## Part 2: Testing the API

---

### 1. Test Plan Document

Create a comprehensive test plan that includes:

- **Test scope and objectives.**
- **Test scenarios and detailed test cases** covering:
    - All CRUD operations.
    - Validation of each business rule.
    - Boundary conditions (e.g., empty strings, zero values).
    - Negative test cases (invalid category, price, stock, multiple stock updates).
    - Edge cases (very long names, simultaneous stock updates).
- **Test data sets** you plan to use (including 5+ edge cases).
- Any questions or ambiguities you identify.

*Deliverable:* A clear, organized document (Markdown or PDF).

---

### 2. Automated Test Suite

Implement automated tests with these requirements:

- Use any framework or language you prefer (pytest, Jest, Postman/Newman, etc.).
- Tests must cover **all test cases from your test plan**.
- Include **data-driven testing**: run tests with multiple product data variants.
- Validate correct HTTP codes and response bodies.
- Include tests specifically verifying the **stock update once per day** rule.
- Provide a **README** explaining how to set up and run your tests.
- Ensure tests are idempotent and can run multiple times without manual reset.

*Deliverable:* Source code + README.

---

### 3. Exploratory Testing & Bug Reporting

- Conduct **manual testing sessions** using tools like curl, Postman, or your own scripts.
- Explore unexpected inputs, rapid updates, invalid JSON payloads, and concurrency if possible.
- Document any **bugs, inconsistencies, or surprising behaviors** you encounter.
- For each bug, include:
    - Steps to reproduce.
    - Expected vs actual behavior.
    - HTTP requests/responses or screenshots.
    - Severity and suggested fixes.
- Include suggestions for further testing or API improvements.

*Deliverable:* Exploratory testing report + bug reports.

---

### 4. Test Summary & Reflection Report

Summarize your work including:

- Overview of test coverage.
- Summary of bugs found and their resolution status.
- Any limitations or risks.
- Reflection on:
    - Challenges faced during development and testing.
    - How you approached problem-solving.
    - What you would improve if given more time.
- Suggestions for future improvements to the API or testing process.

*Deliverable:* Final report document.

---

## Bonus (Optional)

- Write a **data generation script** that creates multiple valid and invalid test product JSON files based on the business rules.
- Implement **concurrency tests** simulating multiple simultaneous stock updates on the same product, verifying that the once-per-day rule is enforced correctly.
- Add logging in your API that records stock update attempts with timestamps.

---

## Deliverables Recap

1. **Inventory API source code** with instructions to run.
2. **Test plan document**.
3. **Automated test suite and instructions**.
4. **Exploratory testing and bug reports**.
5. **Test summary and reflection report**.
6. Optional: bonus scripts or concurrency tests.

---
