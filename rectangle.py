class Rectangle:
    """Represents a rectangle defined by width and height and exposes its area and perimeter."""
    
    def __init__(self,width:int|float,height:int|float):
        if width <= 0 or height <= 0:
            raise ValueError(f"Width and height must be positive (got {width}, {height})")
        
        self._width = width
        self._height = height
        
    @property
    def width(self) -> int|float:
        return self._width
    
    @property
    def height(self) -> int|float:
        return self._height    
        
    @property
    def area(self) -> float:
        """Returns the rectangle's area"""
        return self.width * self.height
    
    @property
    def perimeter(self) -> float:
        """Returns the rectangle's perimeter"""
        return 2 * (self.width + self.height)