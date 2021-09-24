class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self,percent_change,is_increased):
        if is_increased == True:
            self.price = self.price*(1+percent_change)
        else:
            self.price = self.price*(1-percent_change)
    def print_info(self):
        print("",self.name+",",self.category+",","$"+str(round(self.price,2)))
