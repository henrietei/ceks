class Ceks:

    def __init__(self, prece=None, daudzums=None, cena=None):
        self.prece=prece
        self.daudzums=daudzums
        self.cena=cena

    def get_data(self):
        print (f"{self.prece} \n{self.cena} X {self.daudzums} GAB {Ceks.reciept_count}")
        

    





print(f"SIA MK TRADE \nVeikals RD Electronics \nDārzu iela 14a, Rēzekne, t. 438473 \nKase Nr.2, Šas. Nr. 472493473 \nKrasta iela 105A \nRīga, LV-1019\n {Ceks.reciept_count}")

ceks1=Ceks("virtuves kombains", 1, 58.99)
ceks2=Ceks("blenderis", 2, 49.99)
ceks1.get_data()
ceks2.get_data()