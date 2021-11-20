import os.path
def addPainting():
    while True:
        melyik_fajl=input("\n\tMelyik fájlban szeretnél menteni, ird be a nevét: ")
        if os.path.isfile(melyik_fajl):
            break
        print("\tNem létezik a fájl, próbáld újra!")
    f=open(melyik_fajl, 'a')
    festmenynev=input("\tÍrd be a festmény nevét: ")
    festmenyar=input("\tÍrd be a festmény árát[Ft]: ")
    f.write(f'{festmenynev};{festmenyar}\n')
    f.close()
    print("\tMentve")
    input("\tMenübe való vissza téréshez nyomj Entert!")

addPainting()