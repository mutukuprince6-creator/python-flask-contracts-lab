#!/usr/bin/env python3
"""
Flask Contracts Management Application

This application provides REST API endpoints for managing contracts and customers.
It demonstrates proper HTTP status codes and data privacy practices by returning
sensitive customer information only as existence confirmations (204 No Content).


"""

from flask import Flask, request, current_app, g, make_response

# Sample contract data with unique IDs and contract information
# In production, this would be loaded from a database
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a business"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

# Sample customer data (names only for privacy protection)
# Customer details are sensitive and not exposed through API endpoints
customers = ["bob", "bill", "john", "sarah"]

# Initialize Flask application
app = Flask(__name__)


@app.route('/contractor_info', methods=['GET'])
def contractor_info():
    """
    Retrieve all contracts and total count.
    
    Returns:
        dict: JSON object containing contracts array and total count
        int: HTTP 200 OK status code
    """
    return {
        "contractors": contracts,
        "total_contracts": len(contracts)
    }, 200


@app.route('/customer_info', methods=['GET'])
def customer_info():
    """
    Retrieve all customer names and total count.
    
    Returns:
        dict: JSON object containing customers array and total count
        int: HTTP 200 OK status code
    """
    return {
        "customers": customers,
        "total_customers": len(customers)
    }, 200


@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    """
    Retrieve a specific contract by its ID.
    
    Args:
        id (int): The contract ID to search for
    
    Returns:
        dict: Contract information if found
        int: HTTP 200 OK if contract exists
        
        OR
        
        dict: Error message
        int: HTTP 404 NOT FOUND if contract doesn't exist
    
    Example:
        GET /contract/1 -> Returns contract with id 1
        GET /contract/99 -> Returns 404 error
    """
    # Search for contract matching the provided ID using generator expression
    contract = next((c for c in contracts if c["id"] == id), None)
    
    # Return contract if found, otherwise return 404 error
    if contract:
        return contract, 200
    return {"error": "Contract not found"}, 404


@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):
    """
    Check if a customer exists without exposing sensitive data.
    
    Args:
        customer_name (str): The customer name to search for
    
    Returns:
        str: Empty string (no content)
        int: HTTP 204 NO CONTENT if customer exists
        
        OR
        
        dict: Error message
        int: HTTP 404 NOT FOUND if customer doesn't exist
    
    Design Rationale:
        - Returns 204 (No Content) to confirm customer existence
        - Does NOT return customer data to protect privacy
        - Case-insensitive search for better UX
    
    Example:
        GET /customer/bob -> Returns 204 (customer exists)
        GET /customer/unknown -> Returns 404 (customer not found)
    """
    # Perform case-insensitive customer name lookup
    if customer_name.lower() in [c.lower() for c in customers]:
        # Customer found: return 204 No Content (empty response body)
        return '', 204
    
    # Customer not found: return 404 error
    return {"error": "Customer not found"}, 404


if __name__ == '__main__':
    # Run Flask development server on port 5555 with debug mode enabled
    app.run(port=5555, debug=True)
