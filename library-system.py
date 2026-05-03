import uuid

class Book:
    """Represents a borrowable book with controlled availability state. 
    Ensures that borrowing and returning operations respect the current availability.
    """
    
    def __init__(self,title:str,author:str,available:bool=True):
        self._title = title
        self._author = author
        self._is_available = available
        self._id = uuid.uuid4()
        
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def author(self) -> str:
        return self._author
    
    @property
    def is_available(self) -> bool:
        return self._is_available
    
    def borrow(self) -> None:
        """Changes the state of availability when is borrowed"""
        if not self._is_available:
            raise ValueError("Book is already borrowed.")
        self._is_available = False
    
    def return_book(self) -> None:
        """Changes the state of availability when is returned"""
        if self._is_available:
            raise ValueError("Book is already returned.")
        self._is_available = True