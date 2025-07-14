class TaskNode:
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority
        self.next = None


class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, name: str, priority: int) -> None:
        """Добавляет задачу в конец списка."""
        new_task = TaskNode(name, priority)
        if self.head is None:
            self.head = new_task
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_task

    def remove_task(self, name: str) -> None:
        """Удаляет задачу по названию."""
        if self.head is None:
            print("Список задач пуст.")
            return

        if self.head.name == name:
            self.head = self.head.next
            print(f"Задача '{name}' удалена.")
            return

        current = self.head
        prev = None
        while current is not None and current.name != name:
            prev = current
            current = current.next

        if current is None:
            print(f"Задача '{name}' не найдена.")
        else:
            prev.next = current.next
            print(f"Задача '{name}' удалена.")

    def print_tasks(self) -> None:
        """Выводит список задач в порядке добавления."""
        if self.head is None:
            print("Список задач пуст.")
            return

        current = self.head
        print("Список задач:")
        while current is not None:
            print(f"- {current.name} (приоритет: {current.priority})")
            current = current.next


if __name__ == "__main__":
    todo_list = TaskList()

    todo_list.add_task("Купить продукты", 2)
    todo_list.add_task("Сделать домашнюю работу", 1)
    todo_list.add_task("Позвонить другу", 3)
  
    todo_list.print_tasks()
    # Список задач:
    # - Купить продукты (приоритет: 2)
    # - Сделать домашнюю работу (приоритет: 1)
    # - Позвонить другу (приоритет: 3)

    # Удаляем задачу
    todo_list.remove_task("Сделать домашнюю работу")
    # Вывод: Задача 'Сделать домашнюю работу' удалена.

    # Выводим обновленный список
    todo_list.print_tasks()
    # Список задач:
    # - Купить продукты (приоритет: 2)
    # - Позвонить другу (приоритет: 3)

    # Пытаемся удалить несуществующую задачу
    todo_list.remove_task("Починить машину")
