from Class_unittest_more.Operator.Exception_error import MyException

class operator():
    """Sum, subs, division"""

    def suma(a, b):
        for n in (a, b):
            if not isinstance(n, int) and not isinstance(n, float):
                raise MyException("Error Summa, values must be int or float")
        return a + b

    def substraction(a, b):
        for n in (a, b):
            if not isinstance(n, int) and not isinstance(n, float):
                raise MyException("Error Substraction, values must be int or float")
        return a - b

    def div(a, b):
        try:
            return a/b
        except ZeroDivisionError:
            raise MyException ("Error division por cero")




