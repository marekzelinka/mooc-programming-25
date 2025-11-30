class Person:
    def __init__(self, name: str, email: str) -> None:
        self.name: str = name
        self.email: str = email

    def update_email_domain(self, new_domain: str) -> None:
        old_domain = self.email.split("@")[1]
        self.email = self.email.replace(old_domain, new_domain)


class Student(Person):
    def __init__(self, name: str, id: str, email: str, credits: int) -> None:
        super().__init__(name, email)
        self.id: str = id
        self.credits: int = credits


class Teacher(Person):
    def __init__(self, name: str, email: str, room: str, teaching_years: int) -> None:
        super().__init__(name, email)
        self.email: str = email
        self.teaching_years: int = teaching_years


if __name__ == "__main__":
    saul = Student("Saul Student", "1234", "saul@example.com", 0)
    saul.update_email_domain("example.edu")
    print(saul.email)

    tara = Teacher("Tara Teacher", "tara@example.fi", "A123", 2)
    tara.update_email_domain("example.ex")
    print(tara.email)
