class Rectangle:
    """Creates a rectangle defining its dimensions (width and height) and getting its geometric properties (area and perimeter)."""
    
    def __init__(self,width:int|float,height:int|float):
        if width <= 0 or height <= 0:
            raise ValueError(f"Width and height must be positive. Got '{width}','{height}'")
        
        self._width = width
        self._height = height
        
    @property
    def area(self) -> float:
        """Property that returns the area of the rectangle"""
        return self._width * self._height
    
    @property
    def perimeter(self) -> float:
        """Property that returns the perimeter of the rectangle"""
        return 2 * (self._width + self._height)