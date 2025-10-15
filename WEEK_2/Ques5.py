class Employee:
    total_employee = 0
    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.total_employee += 1
    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}")
emp1 = Employee("Mohd Shadab", "Project Manager")
emp2 = Employee("Ravish Kumar", "Program Executive Manager")
emp3 = Employee("Mohd Abbas", "Computer Network Maintenance")
emp1.display_info()
emp2.display_info()
emp3.display_info()
print("Total Number of employees: ", Employee.total_employee)