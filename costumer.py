class Costumer(object):
    def __init__(self,name,address,phone,registered_by):
        self.name=name
        self.address=address
        self.phone=phone
        self.registered_by=registered_by  
    def Show_info(self):
        pass
    
    def Show_owner_info(self,name,adress,phone):
        return name,adress,phone
    
    def save_in_file(self):
        pass