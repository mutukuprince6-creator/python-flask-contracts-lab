# Flask Contracts Management API

A lightweight REST API for managing contracts and customers with privacy-focused design and proper HTTP status codes.

---

##  Features

### API Endpoints

**Get All Contracts**
```
GET /contractor_info → 200 {contractors, total_contracts}
```

**Get Specific Contract**
```
GET /contract/<id> → 200 {contract} | 404 {error}
```

**Get All Customers**
```
GET /customer_info → 200 {customers, total_customers}
```

**Check Customer Existence**
```
GET /customer/<customer_name> → 204 (empty) | 404 {error}
```

---

##  Key Design Principles

- **204 No Content**: Customer endpoint returns empty body to protect sensitive data
- **404 Not Found**: Used for missing resources
- **Case-insensitive**: Customer name lookups are case-insensitive

---

##  Setup

```bash
# Clone and setup
git clone https://github.com/mutukuprince6-creator/python-flask-contracts-lab.git
cd python-flask-contracts-lab

# Install dependencies
pipenv install

# Activate environment
pipenv shell

# Run application
python server/app.py
```

Server runs on `http://localhost:5555`

---

## Testing

```bash
pytest server/testing/app_test.py
```

---

## Project Structure

```
server/
  ├── app.py              # Main Flask application
  └── testing/
      ├── app_test.py     # Unit tests
      └── conftest.py     # Pytest config
```

---

## Resources

- [Flask Docs](https://flask.palletsprojects.com/)
- [REST API Best Practices](https://restfulapi.net/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### Task 2: Determine the Design

#### App Routes:

- `/contract/<id>`
  - **200**: Contract found — return information
  - **404**: Contract not found

- `/customer/<customer_name>`
  - **204**: Customer found — return no information
  - **404**: Customer not found

---

### Task 3: Develop, Test, and Refine the Code

1. Create a **feature branch**.
2. Build the following routes:

#### `/contract/<id>`

- If the contract ID is found in the given array:
  - Return contract information with a **200** response.
- If not found:
  - Return a **404** response.

#### `/customer/<customer_name>`

- If the customer name is found:
  - Return a **204** response with an empty body.
- If not found:
  - Return a **404** response.

3. Push the feature branch and open a PR on GitHub.
4. Merge into `main`.

---

### Task 4: Document and Maintain

#### Best Practices:

- Add comments to explain logic and purpose.
- Clarify code intent for other developers.
- Include a screenshot of completed work in the README.
- Update the README to reflect functionality using [https://makeareadme.com](https://makeareadme.com).
- Delete stale branches on GitHub.
- Remove unnecessary or commented-out code.
- Update `.gitignore` if needed to exclude sensitive data
