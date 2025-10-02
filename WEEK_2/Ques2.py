class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is Empty"
    def peek(self):
        if not self.items.is_empty():
            return self.items[-1]
        else:
            return "Stack is Empty"
    def size(self):
        return len(self.items)
    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False
class ParkingLot:
    def __init__(self):
        self.Stack = Stack()
    def parkCar(self, plate):
        self.Stack.push(plate)
        print(f"Car {plate} parked")
    def removeCar(self):
        removed = self.Stack.pop()
        print(f"Car {removed} removed from parking lot")
        return removed
    def displayLot(self):
        print("Parking Lot", self.Stack.items)
parkingLot = ParkingLot()
parkingLot.parkCar("ABC123")
parkingLot.parkCar("XYZ789")
parkingLot.parkCar("LMN456")
parkingLot.displayLot()
parkingLot.removeCar()