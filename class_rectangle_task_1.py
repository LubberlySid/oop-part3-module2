"""
   This program is created for calculating the area amd perimeter of a rectangle
                                                                                """


class Rectangle:
    """
       This class is created for represent the rectangle area and perimeter
                                                                           """
    def __init__(self, side_1, side_2, side_3, side_4):
        """
           In this function we created variables that means the sides of rectangle
                                                                                  """
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.side_4 = side_4

    def area(self):
        """
           In this function we calculate the area of rectangle
                                                              """
        rectangle_area = self.side_1 * self.side_2
        print(f"Rectangle area is {rectangle_area}")

    def perimeter(self):
        """
           In this function we calculate the perimeter of rectangle
                                                                   """
        rectangle_perimeter = (self.side_1 + self.side_2) * 2
        print(f"Rectangle perimeter is {rectangle_perimeter}")


result = Rectangle(2, 4, 2, 4)
result.area()
result.perimeter()
