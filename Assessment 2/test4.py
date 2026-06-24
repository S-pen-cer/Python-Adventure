

class Registry:
    request_count = 0
    #staff_info2 = []
    #staff_cost = 0
    #staff_receipt = []
    def __init__(self):
        self.Date = input("Please input the date")
        self.Name = input("Please input a name")
        self.Staff_ID = input("Please input a Staff ID")
        self.Order_Status = "Pending"
        Registry.request_count += 1
        self.staff_info = []
        self.staff_cost = 0
        self.staff_receipt = []
        #info_set = [self.Date, self.Name, self.Staff_ID, Registry.request_count, self.Order_Status]
        #Registry.staff_info.append (info_set)
        #print(Registry.staff_info)

    def member_order(self):
        #for si in Registry.staff_info:
        item = input("Please enter item")
        if item == "":
            print("Please enter valid item name")
        else:
            price = float(input("Please enter price"))
            if price < 0:
                print ("Please enter valid price.")
            quantity = int(input("Please enter quantity"))
            if quantity < 0:
                print ("Please enter valid quantity.")
            current_cost = price*quantity
            self.staff_cost = current_cost
            self.staff_receipt = [item, self.staff_cost]
            print(self.staff_receipt)

            #print(f"Items:{item} amounts to {current_cost}")

    def update_status(self):
        if self.staff_cost >= 500:
            #for si in Registry.staff_info:
            #si[4]="pppppp"
            self.Order_Status = "Pending"
            print("No change")
            #print (Registry.staff_info)
            #print (si)
        elif self.staff_cost < 500:
            #for si in Registry.staff_info:
            self.Order_Status = "Approved"
            #print(Registry.staff_info)
        self.staff_info = [self.Date, self.Name, self.Staff_ID, Registry.request_count, self.Order_Status]
        print(self.staff_info)
                #print (si)
        #Registry.staff_info.append(info_set)
        #elif Registry.staff_cost < 0:
            #print("Invalid Cost")
        #print(Registry.staff_info)
        #Doesn't print updated Registry.staff_info...Change placement?
    def statistics(self):
        #requests = []
        #requests.append(self.staff_info)
        searches = int(input("Please enter request number."))
        for request in self.staff_info:
            print(request)
        #if Registry.request_count == searches:
            #print(self.staff_info)
            if request == searches:
                print(request)
        #for search in range(searches):

            #Registry.member_order(register1)
            #Registry.update_status(register1)
            #requests.append(register1)
        #print(requests)

registry1 = Registry()
Registry.member_order(registry1)
Registry.update_status(registry1)

registry2 = Registry()
Registry.member_order(registry2)
Registry.update_status(registry2)


#registry3 = Registry()
#Registry.member_order(registry3)
#Registry.update_status(registry3)

Registry.statistics(registry1)
Registry.statistics(registry2)
#Registry.statistics(registry3)

#Note: item:Cost (Registry.staff_receipt) is not in a list, so it might not accurately show
#relationship between employee Registry and their orders (member_order)
#Note: There might be a problem with the way things are indexed; it might be difficult to reference
#them later if they need to be changed






