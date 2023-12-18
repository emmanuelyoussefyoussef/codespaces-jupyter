import time 

hoehe=int(input("wie groß soll die Pyramide sein?"))
zwischenspeicherX=1
zwischenspeicherO=1
spitze=int((hoehe/2))
if hoehe % 2 == 0:
    hoehe = hoehe +1
for i in range(hoehe+1):
    if i <= spitze :
        print("X"*zwischenspeicherX + (" "*(((hoehe*2)-(zwischenspeicherO)-i)) + "O"*zwischenspeicherO ))
        zwischenspeicherX= zwischenspeicherX + 1
        zwischenspeicherO=zwischenspeicherO +1
        time.sleep(0.1)
    if i>=spitze:
        print("X"*zwischenspeicherX + (" "*(((hoehe)-(zwischenspeicherO)+i)) + "O"*zwischenspeicherO ))
        zwischenspeicherX= zwischenspeicherX - 1
        zwischenspeicherO=zwischenspeicherO -1
        time.sleep(0.1)