"""
   In this program we represent a total number of students
                                                          """


class Student:
    """
       In this class we represent info and total number of students
                                                                   """
    total_students = 0

    def __init__(self, name, surname, age, profession):
        """
            We use this method for represent our variables
                                                          """
        self.name = name
        self.surname = surname
        self.age = age
        self.profession = profession
        Student.total_students += 1

    def __str__(self):
        """
           We use this method for output info about our students
                                                                """
        return (f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}\n"
                f"Profession: {self.profession}")

    @classmethod
    def get_info(cls):
        return cls.total_students


students = [
            Student("Ostap", "Hrushetskiy", 18, "automation engineer"),
            Student("Vlad", "Vengrun", 17, "librarian")
            ]

for student in students:
    print(f"Information about student:\n{student}\n")
print(f"Total students:{Student.get_info()}")
