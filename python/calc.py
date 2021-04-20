
class Calc:

    def add(self, a:int, b:int):
        return a + b

    def div(self, a, b):
        try:
            return a / b
        except:
            return "integer division or modulo by zero"

