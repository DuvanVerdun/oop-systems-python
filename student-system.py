from __future__ import annotations
import regex

class Student:
    """The blueprint for creating students. Acts as a container for data (Name and Grades) and defines actions (Add grade and Get average grade) that can be performed on that data"""
    
    def __init__(self,name:str):
        self._name:str
        self.name = name
        self._grades:list[Grade] = []
        
    @property    
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self,value:str) -> None:
        self._validate_name(value)
        self._name = value
        
    @property
    def grades(self) -> tuple[Grade,...]:
        return tuple(self._grades)

    def add_grade(self,student_grade:float,max_grade:int) -> None:
        """Instance method to add a grade to the student grades."""
        self._grades.append(Grade(student_grade,max_grade))
        
    
    def get_average_grade(self) -> float:
        """Instance method to get the average grade of the student"""
        if not self._grades:
            raise ValueError(f"No grades available.")
        return sum(g.percentage for g in self._grades) / len(self._grades)

    def _validate_name(self,name:str) -> None:
        """Helper method to validate a name string"""
        if not name.strip():
            raise ValueError(f"Name input cannot be empty. Got '{name}'")
        pattern = r'[^\s\p{L}\p{M}]'
        clean_name = regex.sub(pattern,'',name)
        if clean_name != name:
            matches = regex.findall(pattern,name)
            readable_matches = "', '".join(matches)
            raise ValueError(f"Student name cannot have numbers or symbols. Got '{name}'. '{readable_matches}' not valid")


class Grade:
    """The blueprint for creating grades. Acts as a container for data (Score and Maximum Score) and define an action (Get percentage) that can be performed on that data"""
    
    __slots__ = ("_score","_max_score")
    
    def __init__(self,score:float,max_score:int):
        if score < 0:
            raise ValueError(f"score cannot be negative. Got '{score}'")
        if max_score <= 0:
            raise ValueError(f"max_score cannot be non positive. Got '{max_score}'")
        if score > max_score:
            raise ValueError(f"score cannot be higher than max_score. Got '{score}' and '{max_score}'")
        
        self._score = score
        self._max_score = max_score
    
    @property
    def percentage(self) -> float:
        """Instance method to get the percentage of a hundred that the score is from the maximum score"""
        return (self._score * 100) / self._max_score