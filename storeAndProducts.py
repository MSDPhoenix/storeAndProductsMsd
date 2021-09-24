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
        print(f"{self.name}, {self.category}, {str(round(self.price,2))}")

class Store:
    def __init__(self,name,product_list=[]):
        self.name = name
        self.product_list = product_list
    def add_product(self,new_product):
        self.product_list.append(new_product)
    def sell_product(self,id):
        print("\nSelling",self.product_list[id].name)
        self.product_list[id].print_info()
        del self.product_list[id]
    def print_product_list(self):
        print("\nProduct List:")
        if len(self.product_list)>0:
            for i in self.product_list:
                i.print_info()
        else:
            print(" No products")
    def inflation(self,percent_increase):
        print("\nInflation:")
        for i in self.product_list:
            i.update_price(percent_increase,True)
            i.print_info()
    def set_clearance(self,category,percent_discount):
        print("\nClearance Sale:")
        for i in self.product_list:
            if i.category == category:
                i.update_price(percent_discount,False)
                i.print_info()

garbanzo = Product("garbanzo beans",1.65,"canned goods")
beets = Product("pickled beets",4.15,"canned goods")
sugar = Product("granulated sugar",2.65,"dry goods")
plumbus = Product("plumbus",65.99,"housewares")

garbanzo.print_info()
garbanzo.update_price(.1,True)
garbanzo.print_info()
garbanzo.update_price(.25,False)
garbanzo.print_info()

qfc = Store("QFC")
qfc.add_product(garbanzo)
qfc.add_product(beets)
qfc.add_product(sugar)
qfc.add_product(plumbus)
qfc.print_product_list()

qfc.inflation(.06)
qfc.set_clearance("canned goods",.40)

qfc.sell_product(0)
qfc.print_product_list()
