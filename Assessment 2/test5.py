
class employee_register:
    Cost = 0
    order_count = 0
    registry_info = []
    receipt = []
    approval_counter = 0
    decline_counter = 0
    pending_counter = 0
    def __init__(self, date, name, id, status):
        self.date = date
        self.name = name
        self.id = id
        self.status = "pending"
        employee_register.registry_info = [self.date, self.name, self.id, self.status]

    def get_order(self):
        item = input("Please enter product name")
        if item == "":
            print("Please enter an item name")
        price = float(input("Please enter product price"))
        if price < 0:
            print("Please enter a valid price")
        quantity = int(input("Please enter quantity"))
        if quantity < 0:
            print("Please enter a valid quantity")
        cost = price * quantity
        employee_register.Cost = cost
        employee_register.receipt = [item, employee_register.Cost]

    def update_status(self):
        if employee_register.Cost < 500:
            self.status = "approved"
        print(employee_register.Cost, self.status)
        employee_register.registry_info = [self.date, self.name, self.id, self.status]

    def order_stats(self):
        if self.status == "approved":
            employee_register.approval_counter += 1
        if self.status == "pending":
            employee_register.approval_counter += 1
        if self.status == "declined":
            employee_register.decline_counter += 1
        print(f"The number of approved orders are {employee_register.approval_counter}")
        print(f"The number of pending orders are {employee_register.pending_counter}")
        print(f"The number of declined orders are {employee_register.decline_counter}")

    def display_all(self):
        employee_register.order_count += 1
        print(employee_register.registry_info)
        print(employee_register.receipt)
        print(f"The number of approved orders are {employee_register.approval_counter}")
        print(f"The number of pending orders are {employee_register.pending_counter}")
        print(f"The number of declined orders are {employee_register.decline_counter}")


    register1 = employee_register("Jan 1", "Roy", "abc12")








