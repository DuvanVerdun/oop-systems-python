import regex

class Student:
    """The blueprint for creating students. Acts as a container for data (Name and Grades) and defines actions (Add grade and Get average grade) that can be performed on that data"""
    
    def __init__(self,name:str):
        invalid_chars = self._validate_name(name)
        if invalid_chars:
            raise ValueError(f"Student name cannot have numbers or symbols. Got '{name}'. '{invalid_chars}' not valid")
        
        self.name = name
        self.grades:list[Grade] = []

    def add_grade(self,student_grade:int,max_grade:int):
        """Instance method to add a grade to the student grades."""
        if student_grade < 0:
            raise ValueError(f"student_grade cannot be negative. Got '{student_grade}'")
        self.grades.append(Grade(student_grade,max_grade))
        
    
    def get_average_grade(self) -> float:
        """Instance method to get the average grade of the student"""
        percentages_list = [g.get_percentage() for g in self.grades]
        average_percentage = self._get_average(percentages_list)
        return average_percentage
            
    def _get_average(self,numbers:list[float]) -> float:
        """Helper method to get the average of a list of numbers"""
        if not numbers:
            raise ValueError(f"Numbers list cannot be empty. Got: '{numbers}'")
        total_sum = sum(numbers)
        total_count = len(numbers)
        average = total_sum / total_count
        return average

    def _validate_name(self,name:str) -> str:
        """Helper method to validate a name string"""
        pattern = r'[^\s\p{L}\p{M}]'
        clean_name = regex.sub(pattern,'',name)
        if clean_name != name:
            matches = regex.findall(pattern,name)
            readable_matches = "', '".join(matches)
            return readable_matches
        return ""


class Grade:
    """The blueprint for creating grades. Acts as a container for data (Score and Maximum Score) and define an action (Get percentage) that can be performed on that data"""
    
    def __init__(self,score:int,max_score:int):
        if max_score <= 0:
            raise ValueError(f"max_score cannot be non positive. Got '{max_score}'")
        
        self.score = score
        self.max_score = max_score
        
    def get_percentage(self) -> float:
        """Instance method to get the percentage of a hundred that the score is from the maximum score"""
        percentage = (self.score * 100) / self.max_score
        return percentage
        