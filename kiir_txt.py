
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


def kiir_txt():
    
    z=1
    while z==1:
        lista=[]
        f=0
        g=2
        r =1
        összes_file = os.listdir()


        nemtalált_file=1
        file_találat=0
        txt="\n\tIrjon be egy fájl nevet: "
        nev_1=input(txt)+".txt"

        if (nev_1 == "vissza.txt"):
            z=0
        else:
        
            összes_file = os.listdir()

            for file_1 in összes_file:
                
                if file_1 == nev_1 :
                    file_találat=2

            if file_találat == 2:  


                for e, file in enumerate (összes_file):    #keresünk az összes fájlban 

                    inputFile_as_string( nev_1, lista)

                    for a, elem_listák in enumerate (lista):  #keresük a fáj listájában 



                        while(r==1):
                            txt2="\tForint vagy Euro?[f/e]: "
                            pénz=input(txt2)

                            if(pénz=="f"):
                                for e , lista_elemek in enumerate (lista):
                                    for k, elemek in enumerate(lista_elemek):

                                        if(elemek==lista_elemek[0]):

                                           
                                            print("\n\tNév:", elemek)
                                        else:
                                            print("\tÁr:", elemek , "Forint")    
                                r=0               
                                    
                                    
                            elif(pénz=="e"):
                                for e , lista_elemek in enumerate (lista):
                                    for k, elemek in enumerate(lista_elemek):

                                        if(elemek==lista_elemek[0]):

                                            
                                            print("\n\tNév:", elemek)
                                        else:
                                            print("\tÁr:", int(elemek)/300 , "Euro")
                                r=0            



                            elif(pénz=="vissza"):
                                r=0

                            else:
                                print("\tNem értem\n")

            else:
                print("\tNincs ilyen file")
kiir_txt()