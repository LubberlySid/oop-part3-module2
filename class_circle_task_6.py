"""
   In this program we calculate length and area of the circle
                                                             """


class Circle:
    """
       In this class we represent calculating area and length circle
                                                                    """
    def __init__(self, pi, radius):
        """
            We use this method for represent our variables
                                                          """
        self.pi = pi
        self.radius = radius

    def length(self):
        """
           In this function we calculate circle length
                                                    """
        circle_length = 2 * self.pi * self.radius
        print(f"Circle length = {circle_length}")

    def area(self):
        """
           In this function we calculate circle area
                                                    """
        circle_area = self.pi * self.radius ** 2
        print(f"Circle area = {circle_area}")


result = Circle(3.14, 6)
result.length()
result.area()
