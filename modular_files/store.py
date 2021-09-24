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
