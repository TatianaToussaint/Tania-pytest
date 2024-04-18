class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, num):
        """

        :rtype: object
        """
        self.result += int(num)  # a = a + b     a+= b

    def divide(self, num):
        self.result /= int(num)

    def multiply(self, num):
        self.result *= int(num)

    def subtract(self, num):
        self.result -= int(num)

