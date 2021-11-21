
from ujfajl import creat_newf
from hozzaadas import addPainting
from törlés import törlés
from modositas import modositas
from main import main




def f1(label):
    #print(label)
    input_words=""
    while True:
        input_words=input("""\n\t1.Új fájl létrehozása
\t2.Festménynév és ár hozzáadása
\t3.Módosítás
\t4.Keresés/Fájlok megtekintése
\t5.Törlés
\tExit
\tMelyiket választja?: """)   

        
        if input_words=="1":
            creat_newf()
        elif input_words=="2":
            addPainting()
        elif input_words=="3":
            modositas()
        elif input_words=="4":
            main()
        elif input_words=="5":
            törlés()
        elif input_words=="exit":
            break
        else:
            print("\tKérem probálja újra!")


f1("Program")

