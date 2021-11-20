import os.path

def creat_newf():
    while True:
        uj_fajl_nev=input("\n\tÍrd be az új fájl nevét: ")
        if os.path.isfile(uj_fajl_nev):
            print("Már létezik!")
            igen_nem=input("\tAkarsz új fájl nevet megadni? [i/n]: ")
            if igen_nem=="n":
                break
            elif igen_nem!="i":
                print("\tNajó... próbáld újra...")
        else:
            open(uj_fajl_nev, 'a').close()
            print("\tFájl létrehozva")
            break
    input("\tMenübe való vissza téréshez nyomj Entert!")

creat_newf()   