"""from datetime import time

laiks=time.fromisoformat('12:57:30+02:01')

print(laiks.tzinfo)
print(laiks.fold)


from datetime import timedelta

delta_object=timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

x=timedelta(hours=3, seconds=110)
print(x)
y=timedelta(hours=2, seconds=30)
print(y)

print("Rezultāts")
print(x+x, x-y, x/y, sep="\n")

#print (delta_object)
#obj=timedelta()
#print(obj)


import datetime

from datetime import timedelta

dienassogad=datetime.datetime(2022,1,1)
sodien=datetime.datetime.now()
print("Šodienas datums:", sodien)
print("Šogad nodzīvotas:", sodien-dienassogad)
print("Rīt būs ", sodien+timedelta(days=1))
print()

print("Šogad ir:", sodien.year, "gads")
print("Šodien ir:", sodien.day, "diena")
print(sodien.strftime("%A"))



from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
#print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	

#from datetime import datetime
import pytz
datetime_object=datetime.now(timezone("Europe/Riga"))
print("Current IST:", datetime_object) 

import pytz

print('Timezones')
for timeZone in pytz.all_timezones_set:
    print(timeZone)

    

from datetime import datetime
from pytz import timezone, common_timezones
import random
for n in range(3):
    zona=random.choice(common_timezones)
    print(f"Laika zona: {zona}")
    laikaZona=datetime.now(timezone(zona))
    print(laikaZona)"""