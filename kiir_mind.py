
import os
összes_file=os.listdir()


def inputFile_as_string(file, lista):
    f= open(file , "r" )
    for sor in f:
        sor= sor[:-1].split(";") 
        lista.append([str(sor[0]), int(sor[1])] )
    f.close()
    return

def inputFile(file, lista):
    f= open (file,"r")
    for sor in f:
        sor=sor[:-1] #mindig string tipusú lesz, levágjuk a végéről az entert #:- vége -1
        lista.append(sor)#stringként befűzzük a listába, mindent sring ként olvasunk be 
    f.close()
    return 


def kiir_mind():
    
    r=1
    while r==1:
        lista=[]
        adatok=[]
        f=0
        g=2
        r =1
        összes_file = os.listdir()

        for e, file in enumerate (összes_file):    #keresünk az összes fájlban 


            if(file[-4:] == ".txt"):   # ha txt 
                
                inputFile_as_string(file,lista) #fájlok tartalmát betesszük a listába; lista tartlamazza minden fájl minden listáját

                for a, elem_listák in enumerate (lista):  #keresük a fáj listájában

                    adatok.append(lista[a])  



        while(r==1):
            txt2="\n\tForint vagy Euro?[f/e]: "
            pénz=input(txt2)

            if(pénz=="f"):
                for e , lista_elemek in enumerate (lista):
                    for k, elemek in enumerate(lista_elemek):

                        if(elemek==lista_elemek[0]):

                            print("\n\tNév:", elemek)
                        else:
                            print("\tÁr:", elemek , "Forint")
               

                            
                    
                    
            elif(pénz=="e"):
                for e , lista_elemek in enumerate (lista):
                    for k, elemek in enumerate(lista_elemek):

                        if(elemek==lista_elemek[0]):

                            print("\n\tNév:", elemek)
                        else:
                            print("\tÁr:", int(elemek)/300 , "Euro")
                            



            elif(pénz=="vissza"):
                r=0

            else:
                print("\tNem értem")

kiir_mind()
