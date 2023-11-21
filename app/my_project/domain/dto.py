from dataclasses import dataclass
from datetime import datetime


@dataclass
class BasketDto:
    """
    Data transfer object for Basket
    """
    id: int

@dataclass
class BasketHasProductDto:
    id: int
    basket_id: int
    product_id: int

@dataclass
class CategoryDto:
    name: str

@dataclass
class CharacteristicDto:
    id: int
    width: int
    length: int
    weight: int

@dataclass
class DeliveryDto:
    id: int
    price: int
    delivery_type_type: str

@dataclass
class DeliveryTypeDto:
    type: str

@dataclass
class ImageDto:
    id: int
    image: str
    product_id: int

@dataclass
class OrderDto:
    id: int
    date: datetime
    user_id: int
    delivery_id: int

@dataclass
class ProductDto:
    id: int
    name: str
    description: str
    price: int
    characteristic_id: int
    category_name: str

@dataclass
class UserDto:
    id: int
    user_name: str
    email: str
    password: str
    create_time: datetime

@dataclass
class OrderHasBasketDto:
    id: int
    order_id: int
    basket_id: int

@dataclass
class ReviewDto:
    id: int
    product_id: int
    response: str
    product: ProductDto



