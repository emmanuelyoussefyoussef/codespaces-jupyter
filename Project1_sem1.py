Zahl1 = int(input("Geben Sie ihre erste Zahl ein:"))

Zahl2 = int(input("Geben Sie ihre zweite Zahl ein:"))
print("hi")
print(Zahl1 * Zahl2)

print("Hello Youssef")
print("Thats a discord test")


print("*****************")
#wurfprogramm 
wuerfe = []

for i in range(6):
    wuerfe.append(int(input("wurf:")))

maxP=wuerfe[0]
minP=wuerfe[0]
summeP=0

for i in range(6):
    if maxP< wuerfe[i]:
        maxP= wuerfe[i]

for i in range(6):
    if minP> wuerfe[i]:
        minP= wuerfe[i]

for i in range(6):
    summeP=summeP+wuerfe[i]

mittelP = summeP/len(wuerfe)

print("Bester wurf:",maxP)

print("Schlechtester wurf:",minP)

print("Durschschnittliche Punktzahl:",mittelP)

countdown = []
for i in range(10,0) :
    countdown.append(i)
for i in range(len(countdown)-1):
    print(countdown[i])

