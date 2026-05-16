from flask import Flask

from flask_cors import CORS

from routes.intern_routes import intern_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)

CORS(app)

# REGISTER BLUEPRINTS

app.register_blueprint(intern_bp)
app.register_blueprint(auth_bp)


# HOME ROUTE

@app.route("/")

def home():

    return {

        "success": True,

        "message": "Intern Portal Backend Running"

    }


# RUN SERVER

if __name__ == '__main__':

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )