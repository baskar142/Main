class OddEven:
    @staticmethod
    def OddEven():
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            return f"{number} is an even number"
        else:
            return f"{number} is an odd number"


