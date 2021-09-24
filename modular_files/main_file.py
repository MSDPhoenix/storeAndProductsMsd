# NINJA BONUS: Modularize your code into 3 separate files

from product import Product
from store import Store

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
