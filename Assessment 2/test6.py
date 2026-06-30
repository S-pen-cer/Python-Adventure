
class Registry:
    total_cost = 0
    order_count = 0
    registry_info = []
    receipt = []
    assigned_id = ""
    approval_counter = 0
    decline_counter = 0
    pending_counter = 0
    def __init__(self):
        self.date = input("Please enter the date")
        self.name = input("Please enter name")
        self.id = input("Please enter ID")
        self.status = "pending"
        #Registry.registry_info = [self.date, self.name, self.id, self.status]

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
        print(self.status)
        #Registry.registry_info = [self.date, self.name, self.id, self.status]
        #print(Registry.registry_info)

    def manual_update(self):
        new_status = input("Please enter new status")
        self.status = new_status
        Registry.registry_info = [self.date, self.name, self.id, self.status]
        #print(Registry.registry_info)
        Registry.order_count += 1
        #Registry.registry_info.remove(self.status)
        #Registry.registry_info.append(new_status)
        #print(Registry.registry_info)

    def assign_id(self):
        id1 = self.name[0:3]
        id2 = self.id[-3:]
        id3 = Registry.order_count
        full_id = id1 + id2 + "-" + str(id3)
        Registry.assigned_id = full_id
        #print(Registry.assigned_id)

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

    def tuple_setup(self):
        order_summary = [Registry.receipt, self.status]
        order_tuple = {Registry.assigned_id: order_summary}
        #print(order_tuple)
        #print is in hashtag because it's not necessary to show the tuple in the output this early

    def display_all(self):
        #Registry.order_count += 1
        print(Registry.registry_info)
        print(Registry.receipt)
        print(f"The Order ID is {Registry.assigned_id}")
        print(f"The number of approved orders are {Registry.approval_counter}")
        print(f"The number of pending orders are {Registry.pending_counter}")
        print(f"The number of declined orders are {Registry.decline_counter}")





#register1 = Registry("Jan 1", "Roy", "abc12", "")
#register2 = Registry("Feb 1", "Gili", "def45", "")
registry1 = Registry()
Registry.get_order(registry1)
Registry.update_status(registry1)
Registry.manual_update(registry1)
Registry.assign_id(registry1)
Registry.order_stats(registry1)
Registry.tuple_setup(registry1)
Registry.display_all(registry1)

registry2 = Registry()
Registry.get_order(registry2)
Registry.update_status(registry2)
Registry.manual_update(registry2)
Registry.assign_id(registry2)
Registry.order_stats(registry2)
Registry.tuple_setup(registry2)
Registry.display_all(registry2)

registry3 = Registry()
Registry.get_order(registry3)
Registry.update_status(registry3)
Registry.manual_update(registry3)
Registry.assign_id(registry3)
Registry.order_stats(registry3)
Registry.tuple_setup(registry3)
Registry.display_all(registry3)

registry4 = Registry()
Registry.get_order(registry4)
Registry.update_status(registry4)
Registry.manual_update(registry4)
Registry.assign_id(registry4)
Registry.order_stats(registry4)
Registry.tuple_setup(registry4)
Registry.display_all(registry4)

'''
print(register2.date)
print(register2.name)
print(register2.id)
print(register2.status)


Registry.get_order(register2)
Registry.update_status(register2)
Registry.manual_update(register2)
Registry.assign_id(register2)
Registry.order_stats(register2)
Registry.tuple_setup(register2)
Registry.display_all(register1)
'''








