"""MODULE: access_request. Contains the access request class"""
import hashlib
import json
from datetime import datetime


class OrderRequest:
    """Class representing one order for a product"""

    def __init__(self, product_id, order_type, delivery_address, phone_number, zip_code):
        self.__product_id = product_id
        self.__delivery_address = delivery_address
        self.__order_type = order_type
        self.__phone_number = phone_number
        self.__zip_code = zip_code
        justnow = datetime.utcnow()
        # self.time_stamp2 = datetime.timestamp(justnow)
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        return "OrderRequest:" + json.dumps(self.__dict__)

    @property
    def delivery_address(self):
        """Property representing the address where the product
        must be delivered"""
        return self.__delivery_address

    @delivery_address.setter
    def delivery_address(self, value):
        self.__delivery_address = value

    @property
    def order_type(self):
        """Property representing the type of order: REGULAR or PREMIUM"""
        return self.__order_type

    @order_type.setter
    def order_type(self, value):
        """
        if type(value) == str:
            if value == "REGULAR" or value == "PREMIUM":
                self.__order_type = value
            else:
                if value.upper() != value:
                    raise OrderManagementException("Order type not valid, must be REGULAR or PREMIUM")
                raise OrderManagementException("Order type not valid, must be REGULAR or PREMIUM")
        else:
            raise OrderManagementException("Type of the value is not valid, must be a STRING")
        """
        self.__order_type = value


    @property
    def phone_number(self):
        """Property representing the clients's phone number"""
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @property
    def product_id(self):
        """Property representing the products  EAN13 code"""
        return self.__product_id

    @product_id.setter
    def product_id(self, value):
        self.__product_id = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def order_id(self):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode(encoding="utf-8")).hexdigest()

    @property
    def zip_code(self):
        """Returns the patient's zip_code"""
        return self.__zip_code

    def to_json(self):
        """Returns the object as a JSON string"""
        return {
            "order_id": self.order_id,
            "product_id": self.product_id,
            "order_type": self.order_type,
            "delivery_address": self.delivery_address,
            "phone_number": self.phone_number,
            "zip_code": self.zip_code,
            "time_stamp": self.time_stamp,
        }
