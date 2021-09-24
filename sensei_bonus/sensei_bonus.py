# SENSEI BONUS: Update the product class to give each product a unique id. Update the sell_product method to accept the unique id.

class Product:
    def __init__(self,id,name,price,category):  #ADDED id
        self.id = id                            #ADDED self.id = id
        self.name = name
        self.price = price
        self.category = category

    def update_price(self,percent_change,is_increased):
        if is_increased == True:
            self.price = self.price*(1+percent_change)
        else:
            self.price = self.price*(1-percent_change)
    def print_info(self):
        print("",self.id,self.name+",",self.category+",","$"+str(round(self.price,2)))

class Store:
    def __init__(self,name,product_list=[]):
        self.name = name
        self.product_list = product_list
    def add_product(self,new_product):
        self.product_list.append(new_product)
        print(len(self.product_list),"product(s) in product list")                                                  #PRINT LENGTH OF PRODUCT LIST 
                                                                    # AFTER ADDING PRODUCT

    def sell_product(self,id_to_be_sold):                          #IS THERE A SIMPLER WAY
                                                                    #TO SELECT PRODUCT
                                                                    #USING UNIQUE ID?

        for i in range(len(self.product_list)):                 #ADDED FOR LOOP
            if self.product_list[i].id == id_to_be_sold:                   #ADDED CONDITIONAL
                print("\nSelling",self.product_list[i].name)    #CHANGED "id" TO "i"
                self.product_list[i].print_info()               #CHANGED "id" TO "i"
                del self.product_list[i]                        #CHANGED "id" TO "i"
                break

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

garbanzo = Product(111,"garbanzo beans",1.65,"canned goods")


beets = Product(222,"pickled beets",4.15,"canned goods")
sugar = Product(333,"granulated sugar",2.65,"dry goods")
plumbus = Product(444,"plumbus",65.99,"housewares")

garbanzo.print_info()
garbanzo.update_price(.1,True)
garbanzo.print_info()
garbanzo.update_price(.25,False)
garbanzo.print_info()

qfc = Store("QFC")
qfc.add_product(garbanzo)

# qfc.print_product_list()    #TEMPORARY
# qfc.sell_product(111)       #TEMPORARY
# qfc.print_product_list()    #TEMPORARY

qfc.add_product(beets)
qfc.add_product(sugar)
qfc.add_product(plumbus)
qfc.print_product_list()

# qfc.inflation(.06)
# qfc.set_clearance("canned goods",.40)

qfc.sell_product(111)
qfc.print_product_list()
