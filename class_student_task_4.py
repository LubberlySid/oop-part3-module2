"""
   In this program we compare students evaluations
                                                  """


class Student:
    """
       This class is created for represent and determine the number of grades
                                                                             """
    def __init__(self, name, grades):
        """
           We use this method for represent our variables
                                                         """
        self.name = name
        self.grades = grades

    def __len__(self):
        """
           We use this method to determine the number of grades
                                                               """
        return len(self.grades)


students = [
            Student("Ostap", [12, 9, 10, 11, 8, 12]),
            Student("Vlad", [11, 11, 8, 12]),
            Student("Peter", [12, 9, 10, 11, 8, 12, 10, 9])
            ]

sorted_students = sorted(students, key=lambda student: len(student.grades), reverse=True)

for learner in sorted_students:
    print(f"Student {learner.name}. Number of grades: {len(learner)}")
