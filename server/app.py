#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contractor_info', methods=['GET'])
def contractor_info():
    """Return contractor/contract information"""
    return {
        "contractors": contracts,
        "total_contracts": len(contracts)
    }, 200

@app.route('/customer_info', methods=['GET'])
def customer_info():
    """Return customer information"""
    return {
        "customers": customers,
        "total_customers": len(customers)
    }, 200

@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    """
    Get a specific contract by ID
    200: Contract found, return information
    404: Contract not found
    """
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract:
        return contract, 200
    return {"error": "Contract not found"}, 404

@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):
    """
    Check if a customer exists
    204: Customer found, no content (sensitive data)
    404: Customer not found
    """
    if customer_name.lower() in [c.lower() for c in customers]:
        return '', 204
    return {"error": "Customer not found"}, 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
