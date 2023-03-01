class MyException(Exception):
    def __init__(self, valor):
        super().__init__(valor)
        self.valor = valor
    def __str__(self):
        return "Error. " +str(self.valor)