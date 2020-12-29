class Garden:

    plant_types = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}

    students_init = ["Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"]
    
    def __init__(self, diagram, students = students_init):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)
        

    def plants(self, student):
       	student_spot = (self.students.index(student) + 1) * 2
       	plant_list = list(''.join(self.diagram[0][student_spot - 2 : student_spot]) +
                          ''.join(self.diagram[1][student_spot - 2 : student_spot]))

       	plants_result = []

       	for p in plant_list:
            plants_result.append(Garden.plant_types[p])

        return plants_result
        

    
