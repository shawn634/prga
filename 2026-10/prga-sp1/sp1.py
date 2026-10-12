import time
import math

#6
#12.10.2026
#


pocet= int(input("jakej bude pocet"))

print("kulicka")

for i in range(pocet):
   time.sleep(0.1)
   print(" " * i + "O")
   
for i in range(pocet):
    time.sleep(0.1)
    print(" " * (pocet - i) + "O")

print("tabulka")

for i in range(1, pocet + 1):
    print(i, i * i, math.sqrt(i))
