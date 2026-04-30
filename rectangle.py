class Rectangle:
    """Blueprint to create a parameter. Defining it by its measures (width and height) and being able to get its geometric properties (area and perimeter)."""
    
    def __init__(self,width:int|float,height:int|float):
        if width <= 0 or height <= 0:
            raise ValueError(f"Width and height must be positive. Got '{width}','{height}'")
        if width == height:
            raise ValueError(f"Width and height of a rectangle cannot be the same. Got '{width}','{height}'")
        
        self._width = width
        self._height = height
        
    @property
    def area(self) -> float:
        """Instance method to get the area of the rectangle"""
        return self._width * self._height
    
    @property
    def perimeter(self) -> float:
        """Instance method to get the perimeter of the rectangle"""
        return 2 * (self._width + self._height)