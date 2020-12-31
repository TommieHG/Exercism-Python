from collections import defaultdict

class School:

    #defaultdict allows for adding keys that were not present before
    def __init__(self):
        self.student_dict = defaultdict(list)

    def add_student(self, name, grade):
        self.student_dict[grade].append(name)

    def roster(self):
        roster_list = []
        
        for k in sorted(self.student_dict):
            roster_list.extend(sorted(self.student_dict[k]))

        return roster_list     

    def grade(self, grade_number):
        return sorted(self.student_dict.get(grade_number, []))
