
class BankException(ValueError):
    def __init__(self, message, *args):
        super(BankException, self).__init__(message, *args)

