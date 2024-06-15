class Triangle:
    @staticmethod
    def area_triangle():
        height = float(input("Height: "))
        breadth = float(input("Breadth: "))

        area_of_triangle = (height * breadth) / 2
        print("Area formula: (Height * Breadth) / 2")
        print("Area of Triangle:", area_of_triangle)

    @staticmethod
    def perimeter_triangle():
        height1 = float(input("height1 : "))
        height1 = float(input("height 2: "))
        breadth = float(input("breadth : "))

        perimeter_of_triangle = height1 + height2 + side3
        print("Perimeter formula: height1 + height2 + breadth")
        print("Perimeter of Triangle:", perimeter_of_triangle)

    @staticmethod
    def triangle():
        Triangle.area_triangle()
        Triangle.perimeter_triangle()
