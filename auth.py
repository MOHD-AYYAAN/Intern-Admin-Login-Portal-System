import jwt
import datetime
from functools import wraps
from flask import request, jsonify
from config import SECRET_KEY


# GENERATE TOKEN

def generate_token(admin_id):

    token = jwt.encode({
        "admin_id": str(admin_id),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, SECRET_KEY, algorithm="HS256")

    return token


# TOKEN REQUIRED DECORATOR

def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'Authorization' in request.headers:

            auth_header = request.headers['Authorization']

            # REMOVE "Bearer "
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:

            return jsonify({
                "success": False,
                "message": "Token Missing"
            }), 401

        try:

            decoded_token = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"]
            )

            request.admin = decoded_token

        except Exception as e:

            return jsonify({
                "success": False,
                "message": "Invalid Token",
                "error": str(e)
            }), 401

        return f(*args, **kwargs)

    return decorated

    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({
                "success": False,
                "message": "Token Missing"
            }), 401

        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        except:
            return jsonify({
                "success": False,
                "message": "Invalid Token"
            }), 401

        return f(*args, **kwargs)

    return decorated