print('Hello World!')
print('This is a test')

class Registry:
    request_count = 0
    staff_info = []
    Cost = 0
    message = ""
    def __init__(self, Date, Name, Staff_ID, Status):
        self.Date = Date
        self.Name = Name
        self.Staff_ID = Staff_ID
        self.Status = Status
        Registry.request_count += 1
        info_sum = [self.Date, self.Name, self.Staff_ID, Registry.request_count, self.Status]
        Registry.staff_info.append(info_sum)
        print(Registry.staff_info)

    #def user_input (self):
        

registry1 = Registry("January 1", "Roy", "ABC123", "None")
registry2 = Registry("February 1", "Lila", "DEF4567", "None")
registry3 = Registry("March 1", "Marg", "GHI890","None")

print(Registry.staff_info[2][3])


'''
print(registry1.Date)
print(registry1.Name)
print(registry1.Staff_ID)
print(registry1.Status)

print(registry2.Date)
print(registry2.Name)
print(registry2.Staff_ID)
print(registry2.Status)
'''

