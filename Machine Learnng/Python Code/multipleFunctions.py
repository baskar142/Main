class MathOperations:
    @staticmethod
    def add(a, b):
        """Addition operation."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Subtraction operation."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Multiplication operation."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Division operation."""
        if b == 0:
            return "Error: Division by zero"
        return a / b