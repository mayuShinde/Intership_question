import json

class Employee:
    def __init__(self, emp_id, name, dept, sal):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.sal = float(sal)

    def yearly_sal(self):
        print("Salery:", self.sal * 12)

    def display(self):
        print("ID:", self.emp_id, "Name:", self.name, "Dept:", self.dept, "Salary:", self.sal)

class Manager(Employee):
    def __init__(self, emp_id, name, dept, sal, team_size):
        super().__init__(emp_id, name, dept, sal)
        self.team_size = int(team_size)

    def bonus(self):
        if self.team_size > 5:
            return self.sal * 12 * 0.10
        else:
            return 0

    def display(self):
        print("ID:", self.emp_id, "Name:", self.name, "Dept:", self.dept, "Salary:", self.sal, "Team Size:", self.team_size, "Bonus:", self.bonus())

class EmployeeSystem:
    def __init__(self):
        self.emps = []

    def add_emp(self, emp_id, name, dept, sal, is_manager=False, team_size=0):
        try:
            if is_manager:
                emp = Manager(emp_id, name, dept, sal, team_size)
            else:
                emp = Employee(emp_id, name, dept, sal)
            self.emps.append(emp)
            self.save()
            print("Added", name)
        except Exception as e:
            print("Error adding employee:", e)

    def search_emp(self, emp_id):
        for emp in self.emps:
            if emp.emp_id == emp_id:
                emp.display()
                emp.yearly_sal()
                return
        print("Employee not found")

    def show_report(self):
        if not self.emps:
            print("No employees")
            return
        sorted_emps = sorted(self.emps, key=lambda x: x.sal, reverse=True)
        for emp in sorted_emps:
            emp.display()
        print("Total Employees:", len(self.emps))

    def save(self):
        data = []
        for e in self.emps:
            emp_data = {
                "type": "Manager" if isinstance(e, Manager) else "Employee",
                "id": e.emp_id,
                "name": e.name,
                "dept": e.dept,
                "sal": e.sal
            }
            if isinstance(e, Manager):
                emp_data["team_size"] = e.team_size
            data.append(emp_data)

        try:
            with open("emps.txt", "w") as f:
                json.dump(data, f)
        except:
            print("Error saving data")

    
def main():
    system = EmployeeSystem()
    while True:
        print("1. Add Employee/Manager")
        print("2. Search by ID")
        print("3. Show Report")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            emp_id = input("Enter ID: ")
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            sal = input("Enter Salary: ")
            is_mgr = input("Is this a Manager? (y/n): ").lower() == "y"
            if is_mgr:
                team_size = input("Enter Team Size: ")
                system.add_emp(emp_id, name, dept, sal, True, team_size)
            else:
                system.add_emp(emp_id, name, dept, sal)
        elif choice == "2":
            emp_id = input("Enter ID to search: ")
            system.search_emp(emp_id)
        elif choice == "3":
            system.show_report()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
