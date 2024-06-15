class EligibilityForMarriage:
    @staticmethod
    def eligible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        if gender == 'Male' and age >= 21:
            return "ELIGIBLE"
        elif gender == 'Female' and age >= 18:
            return "ELIGIBLE"
        else:
            return "NOT ELIGIBLE"

