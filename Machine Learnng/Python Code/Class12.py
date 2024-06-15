class multiplefunctions():
    
    def Subfields():
        SubfieldsInAI=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for sub in SubfieldsInAI:
            print("Sub-fields in AI are:")
            print(sub)
        
        
    def OddEven():
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            return f"{number} is an even number"
        else:
            return f"{number} is an odd number"       
        
 
    def eligible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        if gender == 'Male' and age >= 21:
            return "ELIGIBLE"
        elif gender == 'Female' and age >= 18:
            return "ELIGIBLE"
        else:
            return "NOT ELIGIBLE"
        
    def percentage():
        # Define subject marks
        subject_marks = [98, 87, 95, 95, 93]
        
        # Calculate total marks
        total_marks = sum(subject_marks)
        total_subjects = len(subject_marks)
        
        # Calculate percentage
        percentage = (total_marks / (total_subjects * 100)) * 100
        
        # Print subject marks
        for i, mark in enumerate(subject_marks, start=1):
            print(f"Subject{i}= {mark}")
        
        # Print total marks and percentage
        print(f"Total : {total_marks}")
        print(f"Percentage : {percentage:}")
        
        
    
    def area_triangle():
        height = float(input("Height: "))
        breadth = float(input("Breadth: "))

        area_of_triangle = (height * breadth) / 2
        print("Area of Triangle formula: (Height * Breadth) / 2")
        print("Area of Triangle:", area_of_triangle)

    def perimeter_triangle():
        height1 = float(input("height1: "))
        height2 = float(input("height2: "))
        breadth = float(input("breadth: "))

        perimeter_of_triangle = height1 + height2 + breadth
        print("Perimeter of Triangle formula: height1 + height2 + breadth")
        print("Perimeter of Triangle:", perimeter_of_triangle)
            
                 
 
    
    
