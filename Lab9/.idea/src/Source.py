from Classes.Classes import Accounting, Stuff, Buyer

apple = Accounting("apple", 10, 20)
pineapple = Stuff("pineapple", 50, 100, 1)
game = Stuff("game", 1 ,1000,1)
items = [pineapple, game]
buyer = Buyer("Zack", items)

buyer.show()