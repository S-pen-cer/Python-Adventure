from test1 import Registry

'''
Staff_Info = []
def add_requisition (self):
    date = input("Please enter date")
    name = input("Please enter name")
    staff_id = input("Please enter staff ID")
    staff_info = [date, name, staff_id]
    Staff_Info.append(staff_info)
    print (Staff_Info)

add_requisition(Staff_Info)
'''
#tried something previously, might come back later, this is still a draft
def shopping_list(self):
    for si in Registry.staff_info:
        item=input("Please enter item")
        price=float(input("Please enter price"))
        quantity=int(input("Please enter quantity"))
        cost=price*quantity
        Registry.Cost=cost
        if Registry.Cost >= 500:
            Registry.message="Pending"
            for self.Status in si:
                self.Status = Registry.message
        else:
            Registry.message="Approved"
            for self.Status in si:
                self.Status = Registry.message
        #print(f"Item: {item}, Total Cost: {Registry.Cost}")
        #this works, for now; now to think how to connect this to status

'''
def status_update(self):
    #message = "" would this work, instead of a class variable?
    if Registry.Cost >= 500:
        Registry.message="Pending"
        for  [:3] in Registry.staff_info
    else:
        Registry.message="Approved"

    print(Registry.message)

#status_update(registry1
              #might need more tinkering, output doesn't reflect intention I think
'''

shopping_list()


