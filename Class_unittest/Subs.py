class MyException(Exception):
    def __init__(self, valor):
        super().__init__(valor)
        self.valor = valor
    def __str__(self):
        return "Error. " +str(self.valor)

#this method reaises an exception with a personal message
def substraction(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise MyException("Must be int or float")
    return a - b


