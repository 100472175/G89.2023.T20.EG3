"""Module """
import math
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException


class OrderManager:
    """Class for providing the methods for managing the orders"""

    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13):
        """
                This function validates the EAN13 code.
                :param eAn13:
                :return:
        """
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


    def register_order(self, product_id, order_type, address, phone_number, zip_code):
        # Returns a string representing AM-FR-01-O1
        # On errors, returns a VaccineManagementException according to AM-FR-01-O2
        check_type = False
        if type(order_type) == str:
            if (order_type == "REGULAR" or order_type == "PREMIUM"):
                check_type = True
            else:
                if order_type.upper() != order_type:
                    raise OrderManagementException("Order type not valid, must be REGULAR or PREMIUM")
                raise OrderManagementException("Order type not valid, must be REGULAR or PREMIUM")
        else:
            raise OrderManagementException("Type of the order_type is not valid, must be a STRING")

        check_address = False
        if type(address) == str:
            if len(address) <= 100:
                if len(address) > 20:
                    if " " in address:
                        addres_list = address.split(" ")
                        if len(addres_list) > 1:
                            check_address = True
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

        check_phone_number = False
        if type(phone_number) == str:
            if phone_number.isdigit():
                if len(phone_number) == 9 or (len(phone_number) == 12 and phone_number[0:3] == "+34"):
                    check_phone_number = True
                elif len(phone_number) > 9:
                    raise OrderManagementException("Phone number not valid, must have less than 10 characters")
                elif len(phone_number) < 9:
                    raise OrderManagementException("Phone number not valid, must have more than 8 characters")
                else:
                    raise OrderManagementException("Phone number not valid, must have 9 characters")
            else:
                raise OrderManagementException("Phone number not valid, must be numeric")

        if zip_code.isdigit():
            if len(zip_code) == 5:
                if int(zip_code) < 1000:
                    raise OrderManagementException("Zip code not valid, must be greater or equal than 01000")
                elif int(zip_code) > 53000:
                    raise OrderManagementException("Zip code not valid, must be less than 53000")
                check = True
            elif len(zip_code) > 5:
                raise OrderManagementException("Zip code not valid, must have less than 6 digits")
            elif len(zip_code) < 5:
                raise OrderManagementException("Zip code not valid, must have more than 4 digits")
        else:
            raise OrderManagementException("Zip code not valid, must be numeric in the range {01000-52999}")



        if check:
            if self.validate_ean13(product_id):
                my_order = OrderRequest(product_id, order_type, address, phone_number, zip_code)

        # if everything is ok, it will save into the file
        # my_order.save_order()
        return my_order.order_id

    def send_product(self, input_file):
        pass
        # The input file is a string with the file path described in AM-FR-02-I1
        # Returns a String in hexadecimal which represents the tracking number (key that will be needed for AM-FR-02-O1 an AM-FR-02-02)
        # In case of error, it returns an OrderManagementException described in AM-FR-02-O3
