# Write your solution here:
class Task:
    ID_COUNTER = 0

    def __init__(
        self,
        description: str,
        programmer: str,
        workload: int,
    ) -> None:
        self.description: str = description
        self.workload: int = workload
        self.programmer: str = programmer
        self.__finished = False

        Task.ID_COUNTER += 1

        self.id: int = Task.ID_COUNTER

    def __str__(self) -> str:
        workload = f"{self.workload} hours"
        programmer = f"programmer {self.programmer}"
        status = "finished" if self.__finished else "not finished"

        return (
            f"{self.id}: {self.description} ({workload}), {programmer} {status.upper()}"
        )

    def is_finished(self) -> bool:
        return self.__finished

    def mark_finished(self) -> None:
        self.__finished = True


class OrderBook:
    def __init__(self) -> None:
        self.__orders: dict[int, Task] = {}

    def add_order(self, description: str, programmer: str, workload: int) -> None:
        task = Task(description, programmer, workload)

        self.__orders[task.id] = task

    def all_orders(self) -> list[Task]:
        return list(self.__orders.values())

    def programmers(self) -> list[str]:
        return list(set(task.programmer for task in self.__orders.values()))

    def mark_finished(self, id: int) -> None:
        task = self.__orders.get(id)

        if not task:
            raise ValueError(f"Task with id of {id} not found")

        task.mark_finished()

    def finished_orders(self) -> list[Task]:
        return [task for task in self.__orders.values() if task.is_finished()]

    def unfinished_orders(self) -> list[Task]:
        return [task for task in self.__orders.values() if not task.is_finished()]

    def status_of_programmer(self, programmer: str) -> tuple[int, int, int, int]:
        assignet_tasks = [
            task for task in self.__orders.values() if task.programmer == programmer
        ]

        if not assignet_tasks:
            raise ValueError("No programmer with given name")

        finished_tasks = [task for task in assignet_tasks if task.is_finished()]
        unfinished_tasks = [task for task in assignet_tasks if not task.is_finished()]

        finished_tasks_count = len(finished_tasks)
        unfinished_tasks_count = len(assignet_tasks) - finished_tasks_count
        sum_of_finished_workloads = sum(task.workload for task in finished_tasks)
        sum_of_unfinished_workloads = sum(task.workload for task in unfinished_tasks)

        return (
            finished_tasks_count,
            unfinished_tasks_count,
            sum_of_finished_workloads,
            sum_of_unfinished_workloads,
        )


if __name__ == "__main__":
    # t1 = Task("program hello world", "Eric", 3)
    # print(t1.id, t1.description, t1.programmer, t1.workload)
    # print(t1)
    # print(t1.is_finished())
    # t1.mark_finished()
    # print(t1)
    # print(t1.is_finished())
    # t2 = Task("program webstore", "Adele", 10)
    # t3 = Task("program mobile app for workload accounting", "Eric", 25)
    # print(t2)
    # print(t3)

    # print()
    # print()

    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # for order in orders.all_orders():
    #     print(order)

    # print()

    # for programmer in orders.programmers():
    #     print(programmer)

    # print()
    # print()

    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # orders.mark_finished(1)
    # orders.mark_finished(2)

    # for order in orders.all_orders():
    #     print(order)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
