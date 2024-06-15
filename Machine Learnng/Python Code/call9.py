class Angle:
    @staticmethod
    def area_triangle():
        height = float(input("Height: "))
        breadth = float(input("Breadth: "))

        area_of_triangle = (height * breadth) / 2
        print("Area formula: (Height * Breadth) / 2")
        print("Area of Triangle:", area_of_triangle)

    @staticmethod
    def perimeter_triangle():
        side1 = float(input("Side 1: "))
        side2 = float(input("Side 2: "))
        side3 = float(input("Side 3: "))

        perimeter_of_triangle = side1 + side2 + side3
        print("Perimeter formula: Side1 + Side2 + Side3")
        print("Perimeter of Triangle:", perimeter_of_triangle)

    @staticmethod
    def triangle():
        Triangle.area_triangle()
        Triangle.perimeter_triangle()
