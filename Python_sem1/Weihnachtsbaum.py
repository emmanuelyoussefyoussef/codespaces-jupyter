import time

print("Willkommen zum Weihnachtsbaum Projekt!!")
print("""
         *
        ***
       *****
      *******
     *********
    ***********
         *
         *
      """)
#speicher für die Sterne zum ausdrucken
zwischenspeicher=1
x=0
#Eingabe der Größe des Baumes
groesse=int(input("Wie groß soll der Weihnachtsbaum sein?"))
for x in range(groesse):
    #Der erste befehl in print sorgt für den Abstand und der zweite für die Sterne
    print(" " * (groesse - 1*x), zwischenspeicher * "*")
    #Sterne anz7ahl erhöht sich jeden durchlauf
    zwischenspeicher = zwischenspeicher + 2
    #Delay
    time.sleep(0.5)
    #Neue schleife die den Ast printet
    if x == groesse-1:
        if groesse > 4:
            print(" " *(groesse), "*")
            print(" " *(groesse), "*")
            time.sleep(1)
        else :
            print(" " *(groesse), "*")
            time.sleep(1)