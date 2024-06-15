class Triangle:
    def area_triangle(self):
        height = float(input("Height: "))
        breadth = float(input("Breadth: "))

        area_of_triangle = (height * breadth) / 2
        print("Area of Triangle formula: (Height * Breadth) / 2")
        print("Area of Triangle:", area_of_triangle)

    def perimeter_triangle(self):
        side1 = float(input("Side 1: "))
        side2 = float(input("Side 2: "))
        side3 = float(input("Side 3: "))

        perimeter_of_triangle = side1 + side2 + side3
        print("Perimeter of Triangle formula: Side1 + Side2 + Side3")
        print("Perimeter of Triangle:", perimeter_of_triangle)
