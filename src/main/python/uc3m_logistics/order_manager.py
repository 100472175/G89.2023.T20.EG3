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
        if type(order_type) == str:
            if (order_type == "REGULAR" or order_type == "PREMIUM"):
                if self.validate_ean13(product_id):
                    my_order = OrderRequest(product_id, order_type, address, phone_number, zip_code)
            else:
                if order_type.upper() != order_type:
                    raise OrderManagementException("Order type not valid, must be REGULAR or PREMIUM")
                raise OrderManagementException("Order type not valid, must be REGULAR or PREMIUM")
        else:
            raise OrderManagementException("Type of the order_type is not valid, must be a STRING")

        # if everything is ok, it will save into the file
        # my_order.save_order()
        return my_order.order_id

    def send_product(self, input_file):
        pass
        # The input file is a string with the file path described in AM-FR-02-I1
        # Returns a String in hexadecimal which represents the tracking number (key that will be needed for AM-FR-02-O1 an AM-FR-02-02)
        # In case of error, it returns an OrderManagementException described in AM-FR-02-O3
