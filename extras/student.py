class Student:
    """
    Used to model a university student.
    """

    def __init__(
        self, name: str, student_number: str, credits: int = 0, notes: str = ""
    ) -> None:
        self.name = name
        self.__student_number: str = self.__check_student_number(student_number)
        self.credits = credits
        self.notes = notes

    def __check_student_number(self, student_number: str) -> str:
        if len(student_number) < 5:
            raise ValueError("Student nunber should have at least five characters")

        return student_number

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Name cannot be an empty string")

        self.__name = name

    @property
    def student_number(self) -> str:
        return self.__student_number

    @property
    def credits(self) -> int:
        return self.__credits

    @credits.setter
    def credits(self, credits: int) -> None:
        if credits < 0:
            raise ValueError("Study credits cannot be  below zero")

        self.__credits = credits

    @property
    def notes(self) -> str:
        return self.__notes

    @notes.setter
    def notes(self, notes: str) -> None:
        self.__notes = notes.strip()

    def summary(self):
        print(f"Student {self.name} ({self.student_number}):")
        print(f"- credits: {self.credits}")
        print(f"- notes: {self.notes or 'no notes'}")


if __name__ == "__main__":
    # Passing only the name and the student number as arguments to the constructor
    student1 = Student("Sally Student", "12345")
    student1.summary()

    # Passing the name, the student number and the number of study credits
    student2 = Student("Sassy Student", "54321", 25)
    student2.summary()

    # Passing values for all the parameters
    student3 = Student("Saul Student", "99999", 140, "extra time in exam")
    student3.summary()

    # Passing a value for notes, but not for study credits
    # NB: the parameter must be named now that the arguments are not in order
    student4 = Student("Sandy Student", "98765", notes="absent in academic year 20-21")
    student4.summary()
