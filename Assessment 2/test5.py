
class Registry:
    total_cost = 0
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
        Registry.registry_info = [self.date, self.name, self.id, self.status]

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

    def update_status(self):
        if Registry.total_cost < 500:
            self.status = "approved"
        print(Registry.total_cost, self.status)
        Registry.registry_info = [self.date, self.name, self.id, self.status]

    def order_stats(self):
        if self.status == "approved":
            Registry.approval_counter += 1
        if self.status == "pending":
            Registry.approval_counter += 1
        if self.status == "declined":
            Registry.decline_counter += 1
        print(f"The number of approved orders are {Registry.approval_counter}")
        print(f"The number of pending orders are {Registry.pending_counter}")
        print(f"The number of declined orders are {Registry.decline_counter}")

    def display_all(self):
        Registry.order_count += 1
        print(Registry.registry_info)
        print(Registry.receipt)
        print(f"The number of approved orders are {Registry.approval_counter}")
        print(f"The number of pending orders are {Registry.pending_counter}")
        print(f"The number of declined orders are {Registry.decline_counter}")


register1 = Registry("Jan 1", "Roy", "abc12")
print(register1)








