"""Module """
import hashlib
import math
import os
import json
import re
#from order_request import OrderRequest
#from order_management_exception import OrderManagementException
#from order_shipping import OrderShipping


from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_shipping import OrderShipping


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
        if len(ean13) > 13:
            raise OrderManagementException("Product Id not valid, id too long")
        if ean13.isdigit() is False:
            raise OrderManagementException("Product Id not valid, id must be numeric")

        check_sum: int = 0
        for i in range(len(ean13) - 1):
            current_number = int(ean13[i])
            if i % 2 != 0:
                check_sum += current_number * 3
            else:
                check_sum += current_number
        difference = 10 * math.ceil(check_sum / 10) - check_sum
        if int(ean13[-1]) == difference:
            return True
        else:
            raise OrderManagementException("Product Id not valid, invalid EAN13 code")

    @staticmethod
    def validate_order_type(order_type: str):
        if not isinstance(order_type, str):
            raise OrderManagementException("Type of the order_type is not valid, must be a STRING")
        valid = ["REGULAR","PREMIUM"]
        if (order_type == "REGULAR" or order_type == "PREMIUM"):
            return True
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
                        raise OrderManagementException("Address not valid")
                    raise OrderManagementException("Address not valid, must have a space")
                raise OrderManagementException("Address not valid, must have more than 20 characters")
            raise OrderManagementException("Address not valid, must have less than 100 characters")
        raise OrderManagementException("Address not valid, must be a string")

    @staticmethod
    def validate_phone_number(phone_number: str):
        if not isinstance(phone_number, str):
            raise OrderManagementException("Phone number not valid, must be numeric ")
        if isinstance(phone_number,str):
            if phone_number.isdigit():
                if len(phone_number) == 9:
                    return True
                if len(phone_number) > 9:
                    raise OrderManagementException("Phone number not valid, must have less than 10 characters")
                if len(phone_number) < 9:
                    raise OrderManagementException("Phone number not valid, must have more than 8 characters")
                raise OrderManagementException("Phone number not valid, must have 9 characters")
            if len(phone_number) == 12 and phone_number[0:3] == "+34":
                if phone_number[3:].isdigit():
                    return True
                raise OrderManagementException("Phone number not valid, must be numeric")
            raise OrderManagementException("Phone number not valid, must be numeric")

    @staticmethod
    def validate_zip_code(zip_code: str):
        if not isinstance(zip_code, str):
            raise OrderManagementException("Zip code not valid, must be numeric in the range {01000-52999}")
        if zip_code.isdigit():
            if len(zip_code) == 5:
                if int(zip_code) < 1000:
                    raise OrderManagementException("Zip code not valid, must be greater or equal than 01000")
                if int(zip_code) >= 53000:
                    raise OrderManagementException("Zip code not valid, must be less than 53000")
                return True
            if len(zip_code) > 5:
                raise OrderManagementException("Zip code not valid, must have less than 6 digits")
            if len(zip_code) < 5:
                raise OrderManagementException("Zip code not valid, must have more than 4 digits")
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

    def send_product(self, input_file) -> str:
        # The input file is a string with the file path described in AM-FR-02-I1, OrderID and ContactEmail
        # Returns a String in hexadecimal which represents the tracking number (key that will be needed for AM-FR-02-O1 an AM-FR-02-02)
        # In case of error, it returns an OrderManagementException described in AM-FR-02-O3
        # Get the order_id from the file
        order = None
        try:
            with open(input_file, "r+", encoding="utf-8") as file:
                data_og_json = json.load(file)
                data_og = str(data_og_json)
                pattern = r"[0-9a-f]{32}"
                match = re.finditer(pattern, data_og)
                if not match:
                    raise OrderManagementException("Input file has not Json valid format")
                for m in match:
                    order = m.group(0)
        except FileNotFoundError:
            raise OrderManagementException("Input File not Found")
        except json.decoder.JSONDecodeError:
            raise OrderManagementException("Input file has not Json format")

        regex_found = None
        # pattern = r'[A-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,3}\''
        pattern = r'{\'OrderID\':\s?\'[a-f0-9]{32}\',\s?\'ContactEmail\':\s?\'[A-z0-9.-]+@[A-z0-9]+(\.?[A-z0-9]+)*\.[a-zA-Z]{1,3}\'}'
        match = re.finditer(pattern, data_og)
        for m in match:
            regex_found = m.group(0)
        if not regex_found:
            raise OrderManagementException("Data in JSON has no valid values")

        saved = None
        # Check the data has not been modified
        try:
            with open(self.__order_request_json_store, "r+", encoding="utf-8") as file:
                data = json.load(file)
                data2 = str(data)
                pattern = r"[0-9a-f]{32}"
                match = re.finditer(pattern, data2)
                order_hash = None
                for m in match:
                    if m.group(0) == order:
                        order_hash = m.group(0)
                        break
                if not order_hash:
                    raise OrderManagementException("Data in JSON has no valid values")
                for i in data:
                    for j, k in i.items():
                        if j == "order_id" and k == order_hash:
                            saved = i
                            break
        except FileNotFoundError:
            raise OrderManagementException("Order_Request not Found")
        except json.decoder.JSONDecodeError:
            raise OrderManagementException("JSON has not the expected stucture")

        # print("hey", saved)
        if not saved:
            raise OrderManagementException("Data in JSON has no valid values")

        self.validate_order_type(saved["order_type"])
        self.validate_address(saved["delivery_address"])
        self.validate_phone_number(saved["phone_number"])
        self.validate_zip_code(saved["zip_code"])
        self.validate_ean13(saved["product_id"])

        checker = f'OrderRequest:{{"_OrderRequest__product_id": "{saved["product_id"]}", "_OrderRequest__delivery_address":' \
                  f' "{saved["delivery_address"]}", "_OrderRequest__order_type": "{saved["order_type"]}",' \
                  f' "_OrderRequest__phone_number": "{saved["phone_number"]}", ' \
                  f'"_OrderRequest__zip_code": "{saved["zip_code"]}", "_OrderRequest__time_stamp": {saved["time_stamp"]}}}'
        checker = hashlib.md5(checker.encode(encoding="utf-8")).hexdigest()
        if checker != order:
            raise OrderManagementException("The data has been modified")

        # Finding Email
        email = None
        pattern = r'[A-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,3}\''
        match = re.finditer(pattern, data_og)
        for m in match:
            email = m.group(0)
        email = email[:-1]

        # Redundant check for mail, as tested before
        if not email:
            raise OrderManagementException("Data in JSON has no valid values")

        # Generate an instance of the class OrderShipping
        order_shipping = OrderShipping(saved["product_id"], saved["order_id"], email, saved["order_type"])

        # print tracking_code or signature string or tracking_code:
        tracking_code = order_shipping.tracking_code
        self.validate_tracking_code(tracking_code)

        # Save the order_shipping into the file
        try:
            with open(self.__order_shipping_json_store, "r+", encoding="utf-8") as file:
                data = json.load(file)
                data.append(order_shipping.to_json())
                file.seek(0)
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            raise OrderManagementException("Order file has not been found")

        return tracking_code

    def validate_tracking_code(self, sha256):
        pattern = r'[a-f0-9]{64}'
        match = re.fullmatch(pattern, sha256)
        if not match:
            raise OrderManagementException("Internal processing error")

    def deliver_product(self, tracking_code) -> str:
        # The date_signature is a string with the value described in AM-FR-03-I1
        # Returns a boolean value defined in AM-FR-03-O1 and a file defined in AM-FR-03-O2
        # On errors, returns a VaccineManagementException representing AM-RF -03-O3
        order_shipping = None
        try:
            self.validate_tracking_code(tracking_code)
            with open(self.__order_shipping_json_store, "r", encoding="UTF-8") as database:
                data = json.load(database)
                for i in data:
                    if i["tracking_code"] == tracking_code:
                        order_shipping = i
                        break
        except FileNotFoundError:
            raise OrderManagementException("File not found")
        except json.decoder.JSONDecodeError:
            raise OrderManagementException("JSON has not the expected stucture")

        if not order_shipping:
            raise OrderManagementException("Tracking code not found in the database of requests")

        order_request = None
        try:
            with open(self.__order_request_json_store, "r", encoding="UTF-8") as database:
                database = json.load(database)
            for i in database:
                if i["order_id"] == order_shipping["order_id"]:
                    order_request = i
                    break
        except FileNotFoundError:
            raise OrderManagementException("File not found")
        except json.decoder.JSONDecodeError:
            raise OrderManagementException("JSON has not the expected stucture")

        if not order_request:
            raise OrderManagementException("Order request not found in the database of shipping")

        checker = f'OrderRequest:{{"_OrderRequest__product_id": "{order_request["product_id"]}", "_OrderRequest__delivery_address":' \
                  f' "{order_request["delivery_address"]}", "_OrderRequest__order_type": "{order_request["order_type"]}",' \
                  f' "_OrderRequest__phone_number": "{order_request["phone_number"]}", ' \
                  f'"_OrderRequest__zip_code": "{order_request["zip_code"]}", "_OrderRequest__time_stamp": {order_request["time_stamp"]}}}'
        check_hash = hashlib.md5(checker.encode(encoding="utf-8")).hexdigest()

        if check_hash != order_request["order_id"]:
            raise OrderManagementException("The data has been modified")

        shipping_check = "{alg:" + "SHA-256" + ",typ:" + "UC3M" + ",order_id:" + \
                         order_shipping["order_id"] + ",issuedate:" + str(order_shipping["issued_at"]) + \
                         ",deliveryday:" + str(order_shipping["delivery_day"]) + "}"

        shipping_check_hash = hashlib.sha256(shipping_check.encode()).hexdigest()
        if shipping_check_hash != order_shipping["tracking_code"]:
            raise OrderManagementException("The data has been modified")

    """
    def Validate_Contents(self):
        dictionary = {}
        if "OrderId" not in dictionary:
            raise OrderManagementException("Invalid file name: not order_request.json")
            with open(self.__order_shipping_json_store,"r+",encoding="ut"):
                data = json.load(file)
                data.append(order_shipping.to_json())
                file.seek(0)
                json.dump(data,file,indent=4)
            except Exception as exception:
                raise OrderManagementException("Error writing Order request to file") from exception
            return order_shipping.tracking_id
        
            OTHER WAY
            try: 
                dictionary["OrderId"]
            except:
                raise OrderManagementException("Invalid file name: not order_request.json")
    """


if __name__ == "__main__":
    a = OrderManager()

    my_order = OrderManager()
    my_tracking_code = my_order.send_product("../../JsonFiles/test_01_valid.json")

    my_shipping = OrderShipping("8421691423220", "e01521684a7f9535e9fa098a2b86565f", "example@inf.uc3m.es",
                                "REGULAR").tracking_code
    print(my_shipping)
    # Add an order to order_request.json
    a.register_order("1234567890128", "PREMIUM", "Calle de las tinieblas 1", "123456789", "12345")
    # Add an order to order_shipping.json
    a.send_product("..//stores//Function2.json")
