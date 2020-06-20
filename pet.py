from costumer import Costumer
class Pet(Costumer):
    def __init__(self,name,address,phone,registered_by):
      
      super().__init__(name,address,phone,registered_by)
    
    def Show_info(self):
        pass

    def show_owner_info(self):
        pass
    
    def save_in_file(self):
        pass