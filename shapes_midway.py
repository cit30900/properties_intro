class Shape():

    def __init__(self, side1: float, side2: float):
        """ABSTRACT class - should never be instantiated"""
        self.side1 = side1
        self.side2 = side2
        
    def area(self) -> float:
        pass

    def perimeter(self) -> float:
        pass

class Rectangle(Shape):

    def __init__(self, side1: float, side2: float):
        """Instantiate a new object of class Rectangle."""
        super().__init__(side1, side2)

    def area(self, side1: float, side2: float) -> float:
        """Calculates the area of a rectangle with the formula side1*side2"""
        return side1 * side2
    
    def perimeter(self, side1: float, side2: float) -> float:
        """Calculates the perimeter of a rectangle with the formula side1*2 + side2*2"""
        return side1 * 2 + side2 * 2

class Triangle(Shape):

    def __init__(self, side1: float, side2: float, side3: float, height: float):
        """Instantiate a new object of class Triangle."""
        self.side3 = side3
        self.height = height
        super().__init__(side1, side2)

    def area(self, side3: float, height: float) -> float:
        """Calculates the area of a triangle with the formula side3*height*.5"""
        return side3 * height * .5
    
    def perimeter(self, side1: float, side2: float, side3: float) -> float:
        """Calculates the perimeter of a triangle with the formula side1+side2+side3"""
        return side1 + side2 + side3