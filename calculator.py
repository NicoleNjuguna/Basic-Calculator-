import streamlit as st
import math

# Calculator class
class Calculator:
    def __init__(self):
        self.operations = {}
        self.init()

    def init(self):
        self.operations["+"] = self.add
        self.operations["-"] = self.subtract
        self.operations["*"] = self.multiply
        self.operations["/"] = self.divide

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def add_operation(self, symbol, func):
        self.operations[symbol] = func

    def calculate(self, num1, operation_symbol, num2):
        if operation_symbol not in self.operations:
            return "Error: Invalid operation"
        try:
            return self.operations[operation_symbol](num1, num2)
        except Exception as e:
            return f"Error: {e}"

# Advanced operations
def exponent(base, exp):
    return base ** exp

def square_root(number, _):
    if number < 0:
        return "Error: Negative input for square root"
    return math.sqrt(number)

def logarithm(number, base):
    if number <= 0 or base <= 0 or base == 1:
        return "Error: Invalid input for logarithm"
    return math.log(number, base)

# Streamlit app
st.title("🧮 Simple Scientific Calculator")

calc = Calculator()
calc.add_operation("^", exponent)
calc.add_operation("sqrt", square_root)
calc.add_operation("log", logarithm)

st.write("Select an operation and enter the required numbers.")

operation = st.selectbox("Choose an operation", list(calc.operations.keys()))

num1 = st.number_input("Enter first number", value=0.0, format="%.6f")

# For sqrt, only one number is needed
if operation == "sqrt":
    num2 = 0
else:
    num2 = st.number_input("Enter second number", value=0.0, format="%.6f")

if st.button("Calculate"):
    result = calc.calculate(num1, operation, num2)
    st.success(f"Result: {result}")

st.markdown("---")
st.caption("Developed for Streamlit deployment — supports +, -, *, /, ^, sqrt, and log.")
