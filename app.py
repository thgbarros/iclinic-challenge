import os
from flask import Flask
from flask_pymongo import PyMongo
from src.controller.prescription import routes

application = Flask(__name__)
application.register_blueprint(routes)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' \
                                  + os.environ['MONGODB_PASSWORD'] + '@' \
                                  + os.environ['MONGODB_HOSTNAME'] + ':27017/' \
                                  + os.environ['MONGODB_DATABASE']

mongo = PyMongo(application)
db = mongo.db

if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)


