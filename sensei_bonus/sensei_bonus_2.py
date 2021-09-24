# SENSEI BONUS: Update the product class to give each product a unique id. Update the sell_product method to accept the unique id.

class Product:
    item_count=1
    def __init__(self,name,price,category):  #ADDED id
        self.id = Product.item_count                 #ADDED self.id = id
        Product.item_count +=1
        self.name = name
        self.price = price
        self.category = category

    def update_price(self,percent_change,is_increased):
        if is_increased == True:
            self.price = self.price*(1+percent_change)
        else:
            self.price = self.price*(1-percent_change)
    def print_info(self):
        # print("",self.id,self.name+",",self.category+",","$"+str(round(self.price,2)))
        print(f"{self.id} {self.name} {self.category} ${str(round(self.price,2))}")

class Store:
    def __init__(self,name,product_list={}):
        self.name = name
        self.product_list = product_list
    def add_product(self,new_product):
        self.product_list[str(new_product.id)] = new_product
        print(len(self.product_list),"product(s) in product list")
    def sell_product(self,id_to_be_sold):                          
        print("\nSelling",self.product_list[str(id_to_be_sold)].name)    #CHANGED "id" TO "i"
        self.product_list[str(id_to_be_sold)].print_info()               #CHANGED "id" TO "i"
        del self.product_list[str(id_to_be_sold)]                        #CHANGED "id" TO "i"
    def print_product_list(self):
        print("\nProduct List:")
        if len(self.product_list)>0:
            for key,value in self.product_list.items():
                value.print_info()
        else:
            print(" No products")
    def inflation(self,percent_increase):
        print("\nInflation:")
        for key,value in self.product_list.items():
            value.update_price(percent_increase,True)
            value.print_info()
    def set_clearance(self,category,percent_discount):
        print("\nClearance Sale:")
        for key,value in self.product_list.items():
            if value.category == category:
                value.update_price(percent_discount,False)
                value.print_info()

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

# qfc.print_product_list()    #TEMPORARY
# qfc.sell_product(1)       #TEMPORARY
# qfc.print_product_list()    #TEMPORARY

qfc.add_product(beets)
qfc.add_product(sugar)
qfc.add_product(plumbus)
qfc.print_product_list()

qfc.inflation(.06)
qfc.set_clearance("canned goods",.40)

qfc.sell_product(1)
qfc.print_product_list()
