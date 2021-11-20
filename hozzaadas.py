import os.path
def addPainting():
    while True:
        melyik_fajl=input("\n\tMelyik fájlban szeretne menteni?irja be a nevét, és kiterjesztését: ")
        if os.path.isfile(melyik_fajl):
            break
        print("\tNem létezik a fájl, próbálja újra!")
    f=open(melyik_fajl, 'a')
    festmenynev=input("\tÍrja be a festmény nevét: ")
    festmenyar=input("\tÍrja be a festmény árát[Ft]: ")
    f.write(f'{festmenynev};{festmenyar}\n')
    f.close()
    print("\tMentve\n")
    input("\tMenübe való vissza téréshez nyomjon Entert!\n")

addPainting()