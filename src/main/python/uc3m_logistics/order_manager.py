"""Module """
import math


class OrderManager:
    """Class for providing the methods for managing the orders"""

    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(self, ean13):
        """
        This function validates the EAN13 code.
        :param eAn13:
        :return:
        """
        CheckSum = 0
        for i in range(len(ean13) - 1):
            CurrentNumber = int(ean13[i])
            if i % 2 != 0:
                CheckSum += CurrentNumber * 3
            else:
                CheckSum += CurrentNumber
        Difference = 10 * math.ceil(CheckSum / 10) - CheckSum
        return int(ean13[-1]) == Difference


    def register_order(self, product_id, order_type, address, phone_number, zip_code):
        # Returns a string representing AM-FR-01-O1
        # On errors, returns a VaccineManagementException according to AM-FR-01-O2


        pass

    def send_product (self, input_file):
        # The input file is a string with the file path described in AM-FR-02-I1
        # Returns a String in hexadecimal which represents the tracking number (key that will be needed for AM-FR-02-O1 an AM-FR-02-02)
        # In case of error, it returns an OrderManagementException described in AM-FR-02-O3
