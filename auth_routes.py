
from flask import Blueprint, request, jsonify
from models.intern_model import admin_collection
from Utils.auth import generate_token

auth_bp = Blueprint('auth', __name__)


# CREATE DEFAULT ADMIN
if admin_collection.count_documents({"email": "admin@devobyte.com"}) == 0:

    admin_collection.insert_one({
        "email": "admin@devobyte.com",
        "password": "admin123"
    })


# ADMIN LOGIN API
@auth_bp.route('/admin/login', methods=['POST'])
def admin_login():

    data = request.json

    email = data.get('email')
    password = data.get('password')

    admin = admin_collection.find_one({
        "email": email,
        "password": password
    })

    if not admin:
        return jsonify({
            "success": False,
            "message": "Invalid Email or Password"
        }), 401

    token = generate_token(admin['_id'])

    return jsonify({
        "success": True,
        "message": "Login Successful",
        "token": token
    })