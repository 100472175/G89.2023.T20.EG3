"""Exception for the order_management module"""

class OrderManagementException(Exception):
    """Personalised exception for Order Management"""
    def __init__(self, message):

        self.message = message
        super().__init__(self.message)

    @property
    def message(self):
        """gets the message value"""
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message

    def __str__(self):
        return "Error. " + str(self.message)
