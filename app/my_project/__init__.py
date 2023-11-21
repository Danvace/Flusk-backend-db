from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.my_project.controller import basket_controller, basket_has_product_controller, order_has_basket_controller, category_controller, characteristic_controller, delivery_controller, delivery_type_controller, image_controller, order_controller, product_controller, review_controller, user_controller
