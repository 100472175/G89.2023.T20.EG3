class CalculatorException(Exception):
    def __init__(self, value):
        super().__init__(value)
        self.value = value
    def __str__(self):
        return "Error" + self.value

def sum(a,b):
    for i in (a,b):
        if not isinstance(i, (int, float)):
            raise CalculatorException("Invalid datatype in sum parameter")
    return a + b

