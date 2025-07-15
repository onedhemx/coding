class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("очередь пуста, невозможно выполнить dequeue.")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("очередь пуста, невозможно выполнить peek.")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    q = Queue()
    print("Очередь пуста?", q.is_empty())
    
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    print("Размер очереди:", q.size())
    print("Первый элемент (peek):", q.peek())
    print("Удаленный элемент (dequeue):", q.dequeue())
    print("Удаленный элемент (dequeue):", q.dequeue())
    print("Размер очереди:", q.size())
    print("Очередь пуста?", q.is_empty()
    print("Удаленный элемент (dequeue):", q.dequeue())
    print("Очередь пуста?", q.is_empty())
    
    try:
        print("Удаленный элемент (dequeue):", q.dequeue())
    except IndexError as e:
        print("Ошибка:", e)
