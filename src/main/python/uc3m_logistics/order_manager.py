"""Module """
import math
import os
import json
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException


class OrderManager:
    """Class for providing the methods for managing the orders"""

    def __init__(self):
        #store_path = "C:\\Users\\josep\\Desktop\\UC3M\\2º\\2º Cuatrimestre\\Seguridad en Sistemas Informáticos\\Prácticas\\Práctica 2\\src\\main\\python\\uc3m_logistics\\orders.txt"
        store_path = "../stores"
        current_path = os.path.dirname(__file__)

        self.__order_request_json_store = os.path.join(current_path, store_path, "order_request.json")
        self.__order_shipping_json_store = os.path.join(current_path, store_path, "order_shipping.json")
        self.__order_delivery_json_store = os.path.join(current_path, store_path, "order_delivery.json")
        # Create file if it doesnt exists and initialize it with an empty list
        try:
            if not os.path.exists(self.__order_request_json_store):
                with open(self.__order_request_json_store, "w", encoding="utf-8") as file:
                    file.write("[]")
            if not os.path.exists(self.__order_shipping_json_store):
                with open(self.__order_shipping_json_store, "w", encoding="utf-8") as file:
                    file.write("[]")
            if not os.path.exists(self.__order_delivery_json_store):
                with open(self.__order_delivery_json_store, "w", encoding="utf-8") as file:
                    file.write("[]")

        except FileNotFoundError as exception:
            raise OrderManagementException("Error creating the stores") from exception


    @staticmethod
    def validate_ean13(ean13: str):
        """
                This function validates the EAN13 code.
                :param eAn13:
        """
        if not isinstance(ean13, str):
            raise OrderManagementException("Product Id not valid, id must be a string")
        if len(ean13) < 13:
            raise OrderManagementException("Product Id not valid, id too short")
        elif len(ean13) > 13:
            raise OrderManagementException("Product Id not valid, id too long")
        elif ean13.isdigit() is False:
            raise OrderManagementException("Product Id not valid, id must be numeric")

        CheckSum: int = 0
        for i in range(len(ean13) - 1):
            CurrentNumber = int(ean13[i])
            if i % 2 != 0:
                CheckSum += CurrentNumber * 3
            else:
                CheckSum += CurrentNumber
        Difference = 10 * math.ceil(CheckSum / 10) - CheckSum
        if int(ean13[-1]) == Difference :
            return True
        else:
            raise OrderManagementException("Product Id not valid, invalid EAN13 code")




    @staticmethod
    def validate_order_type(order_type: str):
        if not isinstance(order_type, str):
            raise OrderManagementException("Type of the order_type is not valid, must be a STRING")
        if (order_type == "REGULAR" or order_type == "PREMIUM"):
            return True
        else:
            if order_type.upper() != order_type:
                raise OrderManagementException("Order type not valid, must be REGULAR or PREMIUM")
            raise OrderManagementException("Order type not valid, must be REGULAR or PREMIUM")

    @staticmethod
    def validate_address(address: str):
        if not isinstance(address, str):
            raise OrderManagementException("Address not valid, must be a string")
        if type(address) == str:
            if len(address) <= 100:
                if len(address) > 20:
                    if " " in address:
                        addres_list = address.split(" ")
                        if len(addres_list) > 1:
                            return True
                        else:
                            raise OrderManagementException("Address not valid")
                    else:
                        raise OrderManagementException("Address not valid, must have a space")
                else:
                    raise OrderManagementException("Address not valid, must have more than 20 characters")
            else:
                raise OrderManagementException("Address not valid, must have less than 100 characters")
        else:
            raise OrderManagementException("Address not valid, must be a string")

    @staticmethod
    def validate_phone_number(phone_number: str):
        if not isinstance(phone_number, str):
            raise OrderManagementException("Phone number not valid, must be numeric ")
        if type(phone_number) == str:
            if phone_number.isdigit():
                if len(phone_number) == 9:
                    return True
                elif len(phone_number) > 9:
                    raise OrderManagementException("Phone number not valid, must have less than 10 characters")
                elif len(phone_number) < 9:
                    raise OrderManagementException("Phone number not valid, must have more than 8 characters")
                else:
                    raise OrderManagementException("Phone number not valid, must have 9 characters")
            elif len(phone_number) == 12 and phone_number[0:3] == "+34":
                if phone_number[3:].isdigit():
                    return True
                else:
                    raise OrderManagementException("Phone number not valid, must be numeric")
            else:
                raise OrderManagementException("Phone number not valid, must be numeric")

    @staticmethod
    def validate_zip_code(zip_code: str):
        if not isinstance(zip_code, str):
            raise OrderManagementException("Zip code not valid, must be numeric in the range {01000-52999}")
        if zip_code.isdigit():
            if len(zip_code) == 5:
                if int(zip_code) < 1000:
                    raise OrderManagementException("Zip code not valid, must be greater or equal than 01000")
                elif int(zip_code) >= 53000:
                    raise OrderManagementException("Zip code not valid, must be less than 53000")
                return True
            elif len(zip_code) > 5:
                raise OrderManagementException("Zip code not valid, must have less than 6 digits")
            elif len(zip_code) < 5:
                raise OrderManagementException("Zip code not valid, must have more than 4 digits")
        else:
            raise OrderManagementException("Zip code not valid, must be numeric in the range {01000-52999}")

    def register_order(self, product_id: str, order_type: str, address: str, phone_number: str, zip_code: str) -> str:
        # Returns a string representing AM-FR-01-O1
        # On errors, returns a VaccineManagementException according to AM-FR-01-O2

        self.validate_order_type(order_type)
        self.validate_address(address)
        self.validate_phone_number(phone_number)
        self.validate_zip_code(zip_code)
        self.validate_ean13(product_id)

        # This only returns the hash, does not do anything else
        my_order = OrderRequest(product_id, order_type, address, phone_number, zip_code)
        # if everything is ok, it will save into the file
        try:
            with open(self.__order_request_json_store, "r+", encoding="utf-8") as file:
                data = json.load(file)
                data.append(my_order.to_json())
                file.seek(0)
                json.dump(data, file, indent=4)
        except FileNotFoundError as exception:
            raise OrderManagementException("File not found") from exception


        return my_order.order_id

    def send_product(self, input_file):
        pass
        # The input file is a string with the file path described in AM-FR-02-I1
        # Returns a String in hexadecimal which represents the tracking number (key that will be needed for AM-FR-02-O1 an AM-FR-02-02)
        # In case of error, it returns an OrderManagementException described in AM-FR-02-O3
