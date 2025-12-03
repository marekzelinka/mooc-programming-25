# Write your solution here
# If you use the classes made in the previous exercise, copy them here
# Write your solution here:
class Task:
    ID_COUNTER = 0

    def __init__(
        self,
        description: str,
        programmer: str,
        workload: int,
    ) -> None:
        Task.ID_COUNTER += 1

        self.__id: int = Task.ID_COUNTER
        self.description: str = description
        self.workload: int = workload
        self.programmer: str = programmer
        self.__finished: bool = False

    def __str__(self) -> str:
        workload = f"{self.workload} hours"
        programmer = f"programmer {self.programmer}"
        status = "finished" if self.__finished else "not finished"

        return f"{self.__id}: {self.description} ({workload}), {programmer} {status.upper()}"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def finished(self) -> bool:
        return self.__finished

    def mark_finished(self) -> None:
        self.__finished = True


class OrderBook:
    def __init__(self) -> None:
        self.__tasks: dict[int, Task] = {}

    def add_order(self, description: str, programmer: str, workload: int) -> None:
        task = Task(description, programmer, workload)

        self.__tasks[task.id] = task

    def all_orders(self) -> list[Task]:
        return list(self.__tasks.values())

    def list_programmers(self) -> list[str]:
        return list(set(task.programmer for task in self.__tasks.values()))

    def mark_finished(self, order_id: int) -> None:
        task = self.__tasks.get(order_id)

        if not task:
            raise ValueError(f"Task with id of {order_id} not found")

        task.mark_finished()

    def finished_orders(self) -> list[Task]:
        return [task for task in self.__tasks.values() if task.finished]

    def unfinished_orders(self) -> list[Task]:
        return [task for task in self.__tasks.values() if not task.finished]

    def status_of_programmer(self, programmer: str) -> tuple[int, int, int, int]:
        assignet_tasks = [
            task for task in self.__tasks.values() if task.programmer == programmer
        ]

        if not assignet_tasks:
            raise ValueError("No programmer with given name")

        finished_tasks = [task for task in assignet_tasks if task.finished]
        unfinished_tasks = [task for task in assignet_tasks if not task.finished]

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


class OrderBookApp:
    def __init__(self) -> None:
        self.__running: bool = False
        self.__orderbook: OrderBook = OrderBook()

    def add_order(self, inputs: tuple[str, str, int]) -> None:
        self.__orderbook.add_order(*inputs)

        print("added!")

    def list_finished_tasks(self) -> None:
        finished_tasks = self.__orderbook.finished_orders()

        if not finished_tasks:
            print("no finished tasks")

        self.__print_orders(finished_tasks)

    def list_unfinished_tasks(self) -> None:
        unfinished_tasks = self.__orderbook.unfinished_orders()

        if not unfinished_tasks:
            print("no unfinished tasks")

        self.__print_orders(unfinished_tasks)

    def mark_finished(self, inputs: tuple[int]) -> None:
        self.__orderbook.mark_finished(*inputs)

        print("marked as finished")

    def list_programmers(self) -> None:
        programmers = self.__orderbook.list_programmers()

        for programmer in programmers:
            print(programmer)

    def status_of_programmer(self, inputs: tuple[str]):
        (
            finished_tasks_count,
            unfinished_tasks_count,
            sum_of_finished_workloads,
            sum_of_unfinished_workloads,
        ) = self.__orderbook.status_of_programmer(*inputs)

        print(
            f"tasks: finished {finished_tasks_count} not finished {unfinished_tasks_count}, "
            f"hours: done {sum_of_finished_workloads} scheduled {sum_of_unfinished_workloads}"
        )

    def exit(self) -> None:
        self.__running = False

    def execute(self) -> None:
        self.__running = True

        self.__help()

        while self.__running:
            print()

            command = input("command: ")

            if command == "0":
                self.exit()
            elif command == "1":
                try:
                    self.add_order(self.__add_order_inputs())
                except ValueError:
                    print("erroneous input")
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                try:
                    self.mark_finished(self.__mark_finished_inputs())
                except ValueError:
                    print("erroneous input")
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                try:
                    self.status_of_programmer(self.__status_of_programmer_inputs())
                except ValueError:
                    print("erroneous input")
            else:
                self.__help()

    def __add_order_inputs(self) -> tuple[str, str, int]:
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split(" ")

        return description, programmer, int(workload)

    def __mark_finished_inputs(self) -> tuple[int]:
        id = input("id: ")

        return (int(id),)

    def __status_of_programmer_inputs(self) -> tuple[str]:
        programmer = input("programmer: ")

        return (programmer,)

    def __help(self) -> None:
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def __print_orders(self, orders: list[Task]) -> None:
        for task in orders:
            print(task)


orderbook_app = OrderBookApp()
orderbook_app.execute()
