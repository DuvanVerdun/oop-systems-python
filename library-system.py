import uuid

class BookNotAvailableError(Exception):
    pass

class BookAlreadyReturnedError(Exception):
    pass

class Book:
    """Represents a borrowable book with controlled availability state. 
    Ensures that borrowing and returning operations respect the current availability.
    """
    
    def __init__(self,title:str,author:str,available:bool=True):
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        if not author.strip():
            raise ValueError("Author cannot be empty.")
        
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
    
    @property
    def id(self):
        return self._id
    
    def __eq__(self,other:object) -> bool:
        if not isinstance(other,Book):
            return NotImplemented
        return self._id == other._id
    
    def borrow(self) -> None:
        """Changes the state of availability when is borrowed"""
        if not self._is_available:
            raise BookNotAvailableError("Book is already borrowed.")
        self._set_availability(False)
    
    def mark_as_returned(self) -> None:
        """Changes the state of availability when is returned"""
        if self._is_available:
            raise BookAlreadyReturnedError("Book is already returned.")
        self._set_availability(True)
        
    def __repr__(self) -> str:
        return f"Book(id={self._id}, title='{self._title}', author='{self._author}', available={self._is_available})"
    
    def _set_availability(self,value:bool) -> None:
        self._is_available = value