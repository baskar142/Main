class MathOperations:
    @staticmethod
    def calculate_bmi(weight, height):
        return weight / (height ** 2)

    @staticmethod
    def is_even(number):
        return number % 2 == 0

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    number = int(input("Enter a number to check if it's even: "))

    bmi = MathOperations.calculate_bmi(weight, height)
    even_or_odd = "even" if MathOperations.is_even(number) else "odd"

    print(f"Your BMI is: {bmi}")
    print(f"The number {number} is {even_or_odd}.")

if __name__ == "__main__":
    main()