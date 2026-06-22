

class Registry:
    request_count = 0
    staff_info = []
    staff_cost = 0
    staff_receipt = []
    def __init__(self):#
        self.Date = input("Please input the date")
        self.Name = input("Please input a name")
        self.Staff_ID = input("Please input a Staff ID")
        self.Order_Status = input("Please input current status of order")
        Registry.request_count += 1
        info_set = [self.Date, self.Name, self.Staff_ID, Registry.request_count, self.Order_Status]
        Registry.staff_info.append (info_set)
        print(Registry.staff_info)

    def member_order(self):
        for si in Registry.staff_info:
            item = input("Please enter item")
            if item == "":
                print("Please enter valid item name")
            else:
                price = float(input("Please enter price"))
                if price < 0:
                    print ("Please enter valid price.")
                quantity = int(input("Please enter quantity"))
                current_cost = price*quantity
                Registry.staff_cost = current_cost
                Registry.staff_receipt = [item, Registry.staff_cost]
                print(Registry.staff_receipt)

                #print(f"Items:{item} amounts to {current_cost}")

    def update_status(self):
        if Registry.staff_cost >= 500:
            for si in Registry.staff_info:
                self.Order_Status = "Pending"
                print (Registry.staff_info)
        elif Registry.staff_cost < 500:
            for si in Registry.staff_info:
                self.Order_Status = "Approved"
        elif Registry.staff_cost < 0:
            print("Invalid Cost")
        print(Registry.staff_info)
        #Doesn't print updated Registry.staff_info...Change placement?

register1 = Registry()
Registry.member_order(register1)
Registry.update_status(register1)

#Note: item:Cost (Registry.staff_receipt) is not in a list, so it might not accurately show
#relationship between employee Registry and their orders (member_order)
#Note: There might be a problem with the way things are indexed; it might be difficult to reference
#them later if they need to be changed






