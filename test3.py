

class Registry:
    request_count = 0
    staff_info = []
    staff_cost = 0
    staff_receipt = []
    def __init__(self):
        Date = input("Please input the date")
        Name = input("Please input a name")
        Staff_ID = input("Please input a Staff ID")
        Order_Status = input("Please input current status of order")
        Registry.request_count += 1
        info_set = [Date, Name, Staff_ID, Registry.request_count, Order_Status]
        Registry.staff_info.append (info_set)

    def member_order(self):
        for si in Registry.staff_info:
            item = input("Please enter item")
            if item == "":
                print("Please enter valid item name")
            else:
                price = float(input("Please enter price"))
                quantity = int(input("Please enter quantity"))
                current_cost = price*quantity
                Registry.staff_cost = current_cost

                #print(f"Items:{item} amounts to {current_cost}")

    def update_order(self):
        for si in Registry.staff_info:
            if

registry1 = Registry()
#Seems to work with inputs now; Might be better to put methods in one file instead of multiple
#Note: Class in one file and methods in another is not the same as calling as Class in another
#file. The latter is said to just make a function that uses the Class, and is not a method itself





