import regex

class Student:
    """The blueprint for creating students. Acts as a container for data (Name and Grades) and defines actions (Add grade and Get average grade) that can be performed on that data"""
    
    def __init__(self,name:str):
        
        if not isinstance(name,str):
            raise TypeError(f"Student name must be a string. Got '{name}'. Type: '{type(name).__name__}'")
        invalid_chars = self._validate_name(name)
        if invalid_chars:
            raise ValueError(f"Student name cannot have numbers or symbols. Got '{name}'. '{invalid_chars}' not valid")
        
        self.name = name
        self.grades = []

    def add_grade(self,student_grade:int,max_grade:int):
        """Instance method to add a grade to the student grades."""
        
        if not isinstance(student_grade,int) and not isinstance(max_grade,int):
            raise TypeError(f"Grades must be integers. Got '{student_grade}' and '{max_grade}'. Types: '{type(student_grade).__name__}', '{type(max_grade).__name__}'")
        if not isinstance(student_grade,int) or not isinstance(max_grade,int):
            if not isinstance(student_grade,int):
                invalid_input = student_grade
            if not isinstance(max_grade,int):
                invalid_input = max_grade
            raise TypeError(f"Grades must be integers. Got '{invalid_input}'. Type: '{type(invalid_input).__name__}'")
        
        self.grades.append((student_grade,max_grade))
    
    def get_average_grade(self) -> float:
        """Instance method to get the average grade of the student"""
        percentages_list = self._get_percentages()
        return self._get_average(percentages_list)
    
    def _get_percentages(self) -> list:
        """Helper method to get the list of percentages of the grades of the student"""
        percentages_list = []
        for g in self.grades:
            student = g[0]
            maximum = g[1]
            percentage = (student * 100) / maximum
            percentages_list.append(percentage)
        return percentages_list
            
    def _get_average(self,numbers:list) -> float:
        """Helper method to get the average of a list of numbers"""
        invalid_characters = self._validate_numbers(numbers)
        if invalid_characters:
            raise TypeError(f"Every element in the list provided must be integer or float. Got: {numbers}. {invalid_characters} not valid.")
        total_sum = sum(numbers)
        total_count = len(numbers)
        average = total_sum / total_count
        return average

    def _validate_numbers(self,numbers:list) -> list:
        """Helper method to validate the type of the elements of a list of numbers"""
        if any(not isinstance(n,int) or not isinstance(n,float) for n in numbers):
            invalid_characters = [n for n in numbers if not isinstance(n,int) and not isinstance(n,float)]
            return invalid_characters
        return []

    def _validate_name(self,name:str) -> str:
        """Helper method to validate a name string"""
        pattern = r'[^\s\p{L}\p{M}]'
        clean_name = regex.sub(pattern,'',name)
        if clean_name != name:
            matches = regex.findall(pattern,name)
            readable_matches = "', '".join(matches)
            return readable_matches
        return ""
