class Ceks:

    def __init__(self, prece=None, daudzums=None, cena=None):
        self.prece=prece
        self.daudzums=daudzums
        self.cena=cena

    def get_data(self):
        print (f"{self.prece} \n{self.cena} X {self.daudzums} GAB")
        

file=open("ttt.txt", "r")
str1=(file.readline())
#print(str1)
file=open("ttt.txt","w")
str2=int(str1)+1
file.write(str(str2))
file.close()






print(f"SIA MK TRADE \nVeikals RD Electronics \nDārzu iela 14a, Rēzekne, t. 438473 \nKase Nr.2, Šas. Nr. 472493473 \nKrasta iela 105A \nRīga, LV-1019 \nČeka numurs {str1}")

ceks1=Ceks("virtuves kombains", 1, 58.99)
ceks2=Ceks("blenderis", 2, 49.99)
ceks1.get_data()
ceks2.get_data()

x=ceks1.daudzums*ceks1.cena+ceks2.daudzums*ceks2.cena
y=0.78*x
z=0.21*x


print(f"PVN 21% {z}$\nCena bez PVN {y}$ \nKopā cena {x}$")

