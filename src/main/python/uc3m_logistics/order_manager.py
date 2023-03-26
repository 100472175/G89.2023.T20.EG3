"""Module """
import hashlib
import math
import os
import json
import re
from order_request import OrderRequest
from order_management_exception import OrderManagementException
from order_shipping import OrderShipping


# from .order_request import OrderRequest
# from .order_management_exception import OrderManagementException
# from .order_shipping import OrderShipping


class OrderManager:
    """Class for providing the methods for managing the orders"""

    def __init__(self):
        store_path = "../stores"
        current_path = os.path.dirname(__file__)

        self.__order_request_json_store = os.path.join(current_path, store_path, "order_request.json")
        self.__order_shipping_json_store = os.path.join(current_path, store_path, "order_shipping.json")
        self.__order_delivery_json_store = os.path.join(current_path, store_path, "order_delivery.json")
        # Create file if it doesn't exists and initialize it with an empty list
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
        if int(ean13[-1]) == Difference:
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
        # The input file is a string with the file path described in AM-FR-02-I1, OrderID and ContactEmail
        # Returns a String in hexadecimal which represents the tracking number (key that will be needed for AM-FR-02-O1 an AM-FR-02-02)
        # In case of error, it returns an OrderManagementException described in AM-FR-02-O3
        # Get the order_id from the file
        order = None
        with open(input_file, "r+", encoding="utf-8") as file:
            data_og_json = json.load(file)
            data_og = str(data_og_json)
            pattern = r"[0-9a-f]{32}"
            match = re.finditer(pattern, data_og)
            for m in match:
                order = m.group(0)



        saved = None
        # Check the data has not been modified
        with open(self.__order_request_json_store, "r+", encoding="utf-8") as file:
            data = json.load(file)
            data2 = str(data)
            pattern = r"[0-9a-f]{32}"
            match = re.finditer(pattern, data2)
            for m in match:
                if m.group(0) == order:
                    order_hash = m.group(0)
                    break

            for i in data:
                for j, k in i.items():
                    if j == "order_id" and k == order_hash:
                        saved = i
                        break
        # print("hey", saved)

        checker = f'OrderRequest:{{"_OrderRequest__product_id": "{saved["product_id"]}", "_OrderRequest__delivery_address":' \
                  f' "{saved["delivery_address"]}", "_OrderRequest__order_type": "{saved["order_type"]}",' \
                  f' "_OrderRequest__phone_number": "{saved["phone_number"]}", ' \
                  f'"_OrderRequest__zip_code": "{saved["zip_code"]}", "_OrderRequest__time_stamp": {saved["time_stamp"]}}}'
        # print(a)
        checker = hashlib.md5(checker.encode(encoding="utf-8")).hexdigest()
        # print(a)
        if checker != order:
            raise OrderManagementException("The data has been modified")

        # Generate an instance of the class OrderShipping

        # data_og = data_og

        """patter_alg = r"[a-z0-9]{32}"
        alg = re.findall(patter_alg, data_og)[0]
        self.validate_alg(alg)

        type = "UC3M"
        """
        order_id = checker
        email = ""

        #Email check:
        pattern = r'[A-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,3}'
        match = re.finditer(pattern, data_og)
        for m in match:
            email = m.group(0)



        order_shipping = OrderShipping(saved["product_id"], order_id, email, saved["order_type"])
        # print tracking_code or signature string or tracking_code:
        tracking_code = order_shipping.tracking_code

        # Save the order_shipping into the file
        try:
            with open(self.__order_shipping_json_store, "r+", encoding="utf-8") as file:
                data = json.load(file)
                data.append(order_shipping.to_json())
                file.seek(0)
                json.dump(data, file, indent=4)
        except FileNotFoundError as exception:
            raise OrderManagementException("File not found") from exception




    def Validate_Contents(self):
        dictionary = {}
        if "OrderId" not in dictionary:
            raise OrderManagementException("Invalid file name: not order_request.json")
        """
            with open(self.__order_shipping_json_store,"r+",encoding="ut"):
                data = json.load(file)
                data.append(order_shipping.to_json())
                file.seek(0)
                json.dump(data,file,indent=4)
            except Exception as exception:
                raise OrderManagementException("Error writing Order request to file") from exception
            return order_shipping.tracking_id
        """

        """
            OTHER WAY
            try: 
                dictionary["OrderId"]
            except:
                raise OrderManagementException("Invalid file name: not order_request.json")
            """


if __name__ == "__main__":
    a = OrderManager()
    a.register_order("1234567890128", "PREMIUM", "Calle de las tinieblas 1", "123456789", "12345")
    a.send_product("..//stores//Function2.json")
