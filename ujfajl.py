import os.path

def creat_newf():
    while True:
        uj_fajl_nev=input("\n\tÍrja be az új fájl nevét, és kiterjesztését: ")
        if os.path.isfile(uj_fajl_nev):
            
            
            print("\tA fáj már létezik!\n")
            
            igen_nem=input("\tAkar új fájl nevet megadni?[i/n]: ")
            if igen_nem=="n":
                break
            elif igen_nem!="i":
                print("\tNajó... próbáld újra...")
                
                
        else:
            open(uj_fajl_nev, 'a').close()
            print("\tFájl létrehozva")
            break
    input("\n\tMenübe való vissza téréshez nyomjon Entert!\n")

#creat_newf()   