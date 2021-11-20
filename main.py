from kiir_mind import kiir_mind
from kiir_txt import kiir_txt
from max_file import max_mindenben
from max_txtben import txt_legnagyobb
from min_file import min_mindenben
from min_txtben import min_txt
from kereses_minden import keresés_minden_fájlban
from kereses_txtben import keresés_txt
from atlag_mind import atlag_mindenben
from atlag_txt import atlag_txt

import os
összes_file=os.listdir()


def inputFile_as_string(file, lista):
    f= open(file , "r" )
    for sor in f:
        sor= sor[:-1].split(";")
        lista.append([str(sor[0]), int(sor[1])])
    f.close()
    return


def main():
    x = 0
    while (x==0):
        txt="\tFájl kezelés\n\tMinden fájl kezelés\n\t[f/m]:"
        melyik=input(txt)
       
        y=0   
        while(y==0):
################################################################################################            
            if(melyik== "f"):
                txt1="\tFájlban:\n\t-Keresés\n\t-Mindegyik\n\t-Legnagyobb\n\t-Legkisebb\n\t-Átlag\n\t[s/all/max/min/atlag]:"
                válasz=input(txt1)

                if(válasz=="s"):
                    keresés_txt()

                elif(válasz=="all"):
                    kiir_txt()
                
                elif(válasz=="max"):
                    txt_legnagyobb()
                
                elif(válasz=="min"):
                    min_txt() 
                elif(válasz=="atlag"):
                    atlag_txt()
                
                elif(válasz=="vissza"):
                    y=1
                else:
                    print("\tNem értem\n")
####################################################################################################
            elif(melyik=="m"):
                txt2="\tMinden fájlban:\n\t-Keresés\n\t-Mindegyik\n\t-Legnagyobb\n\t-legkisebb\n\t-Átlag\n\t[s/all/max/min/atlag]:"
                válasz=input(txt2)

                if(válasz=="s"):
                    keresés_minden_fájlban()

                elif(válasz=="all"):
                    kiir_mind()

                elif(válasz=="max"):
                    max_mindenben()
                
                elif(válasz=="min"):
                    min_mindenben()
                elif(válasz=="atlag"):
                    atlag_mindenben()
                
                elif(válasz=="vissza"):
                    y=1
                
                else:
                    print("\tNem értem\n")

            else:
                print("\tNem értem\n")
                y=1     

        if(melyik=="vissza"):
            x=1
                                 
                               
main()