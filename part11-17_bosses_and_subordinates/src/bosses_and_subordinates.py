# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.subordinates: list["Employee"] = []

    def add_subordinate(self, employee: "Employee") -> None:
        self.subordinates.append(employee)


def count_subordinates(employee: Employee) -> int:
    count = len(employee.subordinates)

    for employee in employee.subordinates:
        count += count_subordinates(employee)

    return count


if __name__ == "__main__":
    t1 = Employee("Sally")
    t2 = Employee("Eric")
    t3 = Employee("Matthew")
    t4 = Employee("Emily")
    t5 = Employee("Adele")
    t6 = Employee("Claire")

    t1.add_subordinate(t4)
    t1.add_subordinate(t6)
    t4.add_subordinate(t2)
    t4.add_subordinate(t3)
    t4.add_subordinate(t5)

    print(count_subordinates(t1))
    print(count_subordinates(t4))
    print(count_subordinates(t5))
