import regex

class Student:
    """The blueprint for creating students. Acts as a container for data (Name and Grades) and defines actions (Add grade and Get average grade) that can be performed on that data"""
    
    def __init__(self,name:str):
        self._validate_name(name)
        
        self.name = name
        self.grades:list[Grade] = []

    def add_grade(self,student_grade:int,max_grade:int) -> None:
        """Instance method to add a grade to the student grades."""
        self.grades.append(Grade(student_grade,max_grade))
        
    
    def get_average_grade(self) -> float:
        """Instance method to get the average grade of the student"""
        if not self.grades:
            raise ValueError(f"Not grades available. grades: '{self.grades}'")
        average_percentage = sum(g.percentage for g in self.grades) / len(self.grades)
        return average_percentage

    def _validate_name(self,name:str) -> None:
        """Helper method to validate a name string"""
        if not name:
            raise ValueError(f"Name input cannot be empty. Got '{name}'")
        pattern = r'[^\s\p{L}\p{M}]'
        clean_name = regex.sub(pattern,'',name)
        if clean_name != name:
            matches = regex.findall(pattern,name)
            readable_matches = "', '".join(matches)
            raise ValueError(f"Student name cannot have numbers or symbols. Got '{name}'. '{readable_matches}' not valid")


class Grade:
    """The blueprint for creating grades. Acts as a container for data (Score and Maximum Score) and define an action (Get percentage) that can be performed on that data"""
    
    def __init__(self,score:int,max_score:int):
        if score < 0:
            raise ValueError(f"score cannot be negative. Got '{score}'")
        if max_score <= 0:
            raise ValueError(f"max_score cannot be non positive. Got '{max_score}'")
        if score > max_score:
            raise ValueError(f"score cannot be higher than max_score. Got '{score}' and '{max_score}'")
        
        self.score = score
        self.max_score = max_score
    
    @property
    def percentage(self) -> float:
        """Instance method to get the percentage of a hundred that the score is from the maximum score"""
        percentage = (self.score * 100) / self.max_score
        return percentage
        