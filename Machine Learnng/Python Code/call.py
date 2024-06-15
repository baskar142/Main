class Triangle:
    def area_triangle(self):
        Height = float(input("Height: "))
        Breadth = float(input("Breadth: "))

        area_of_triangle = (height * breadth) / 2
        print("Area formula: (Height * Breadth) / 2")
        print("Area of Triangle:", area_of_triangle)

    def perimeter_triangle(self):
        Height1 = float(input("height 1: "))
        Height2 = float(input("height2 : "))
        Breadth = float(input("width 3: "))

        perimeter_of_triangle = height1 + height2 + Breadth
        print("Perimeter formula: height1 + height2 + Bidth")
        print("Perimeter of Triangle:", perimeter_of_triangle)