class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() == 0
    def __str__(self):
        return str(self.items)
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop() if not self.is_empty() else None
    def front(self):
        return self.items[0] if not self.is_empty() else None
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() == 0
    def __str__(self):
        return str(self.items)
class VehicleMaintenanceLog:
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.print_job = Queue()
        self.current_log = ""
    def add_log(self, text):
        self.undo_stack.push(text)
        self.current_log = text
        self.redo_stack = Stack()
        print(f"Log added: {text}")
    def undo(self):
        if not self.undo_stack.is_empty():
            log = self.undo_stack.pop()
            self.redo_stack.push(log)
            if not self.undo_stack.is_empty():
                self.current_log = self.undo_stack.peek()
            else:
                ""
            print("Undo performed")
        else:
            print("No logs tzo undo")
    def redo(self):
        if not self.redo_stack.is_empty():
            log = self.redo_stack.pop()
            self.undo_stack.push(log)
            self.current_log = log
            print("redo performed")
        else:
            print("No log to redo")
    def add_print_job(self, job):
        self.print_job.enqueue(job)
        print(f"Job Added: {job}")
    def process_print_job(self):
        job = self.print_job.dequeue()
        if job:
            print(f"Processed print job: {job}")
        else:
            print("No Print job")
    def display_state(self):
        print("------x-------------------------System State-------------------------x------")
        print(f"Current Log: {self.current_log}")
        print(f"Undo Stack: {self.undo_stack}")
        print(f"Redo Stack: {self.redo_stack}")
        print(f"Print jobs: {self.print_job}")
        print("-----x----------------------------x---------------------------------x---------------------x")
system = VehicleMaintenanceLog()
system.add_log("Toyota Camry 2020: Oil Change")
system.add_log("Honda Civic 2022: Tire rotation")
system.add_print_job("print toyota camry 2020")
system.add_print_job("print Honda Civic 2022")
system.display_state()
system.undo()
system.add_print_job("Print Summary")
system.redo()
system.process_print_job()
system.display_state()