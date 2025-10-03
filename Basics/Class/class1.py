class Calculator:
    def add(self, a, b):
        self.value = a * b
        return self.value

    def multiply(self, c, d):
        self.value = self.value + c + d
        return self.value

# Create object
calc = Calculator()

# Call method and capture return value
add = calc.add(5, 3)
multiply = calc.multiply(4, 6)
print (add)
print (multiply)
print(calc.value)  # 24
