
class Registry:
    total_cost = 0
    order_count = 0
    registry_info = []
    receipt = []
    assigned_id = ""
    approval_counter = 0
    decline_counter = 0
    pending_counter = 0
    def __init__(self, date, name, id, status):
        self.date = date
        self.name = name
        self.id = id
        self.status = "pending"
        Registry.registry_info = [self.date, self.name, self.id, self.status]

    def assign_id(self):
        id1 = self.name[0:3]
        id2 = self.id[-3:]
        full_id = id1 + id2
        Registry.assigned_id = full_id
        print(Registry.assigned_id)

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
        Registry.total_cost = cost
        Registry.receipt = [item, Registry.total_cost]
        print(Registry.receipt)

    def update_status(self):
        if Registry.total_cost < 500:
            self.status = "approved"
        print(Registry.total_cost, self.status)
        Registry.registry_info = [self.date, self.name, self.id, self.status]
        print(Registry.registry_info)

    def manual_update(self):
        new_status = input("Please enter new status")
        Registry.registry_info [3] = new_status
        print(Registry.registry_info)

'''
    def order_stats(self):
        if self.status == "approved":
            Registry.approval_counter += 1
        if self.status == "pending":
            Registry.pending_counter += 1
        if self.status == "declined":
            Registry.decline_counter += 1
        #print(f"The number of approved orders are {Registry.approval_counter}")
        #print(f"The number of pending orders are {Registry.pending_counter}")
        #print(f"The number of declined orders are {Registry.decline_counter}")

    def display_all(self):
        Registry.order_count += 1
        print(Registry.registry_info)
        print(Registry.receipt)
        print(f"The number of approved orders are {Registry.approval_counter}")
        print(f"The number of pending orders are {Registry.pending_counter}")
        print(f"The number of declined orders are {Registry.decline_counter}")

'''


register1 = Registry("Jan 1", "Roy", "abc12", "")
print(register1.date)
print(register1.name)
print(register1.id)
print(register1.status)

Registry.assign_id(register1)
Registry.get_order(register1)
Registry.update_status(register1)
Registry.manual_update(register1)
Registry.order_stats(register1)
Registry.display_all(register1)








