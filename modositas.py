
import os
összes_file=os.listdir()

def inputFile_as_string(file, lista):
    f= open(file , "r" )
    for sor in f:
        sor= sor[:-1].split(";") 
        lista.append([str(sor[0]), int(sor[1])] )
    f.close()
    return
    
def modositas():
    lista=[] 
    r=1
    while(r==1):
        lista=[]
        f=0
        g=1
        u=1
        c=0
        o=0
        nemtalált_file=1
        file_találat=0
#######################################################################
        txt="\n\tIrjon be egy fájl nevet: "
        nev_1=input(txt)+".txt"
#########################################################################
        if (nev_1 == "vissza.txt"):
            r=0
        else:
            összes_file = os.listdir()
#########################################################################
            for file_1 in összes_file:       
                if file_1 == nev_1 :
                    file_találat=2                              ##keresés
            if file_találat == 2:
                inputFile_as_string( nev_1, lista)
############################################################################
                x =5
                c=0
                while(x != 6):

                    txt= "\n\tMit szeretne modosítani?[n/p]: "
                    d= input(txt)
                    if(  d == "n"):
            ##############################################################
                        c=0
                        while(c != 1):
                            txt="\tIrjon be egy nevet: " 
                            name=input(txt)
                            #print(lista)
                            
            ##############################################################
                            for e , i in enumerate(lista):
                                for f ,b in enumerate(i):               ##Név keresése a listában
                                    if (b == i[0]):
                                        if (name == b):
            ##############################################################   Megvan a név                        txt="\tKérek egy új nevet:"
                                            txt1="\tIrjon be egy új nevet: "
                                            ujnev=input(txt1)
                                            lista[e][f]=ujnev
                                            print("\tKész")
                                            #print(lista)
                                            c = 1
            
                                        elif (name == "vissza"):  ##program végid fut
                                            c=1

                            if(c != 1):
                                txt= "\tNincs ilyen név\n" 
                                print(txt)             
                            
            ################################################################# Név nincs módodsítva                               
                    elif(d == "p"):
                        o=0
                        while(o != 1):
                            c=0
                            txt="\tIrjon be egy nevet: "
                            name=input(txt)
            ######################################################
                            for e , i in enumerate(lista):
                                for f ,b in enumerate(i):               ##Név keresése a listában
                                    if (b == i[0]):
                                        if (name == b):
            ###################################################### Megvan a név                                    
                                            while (c != 1):
                                                txt1="\tEuro vagy Forint?[f/e]: "
                                                q = input(txt1)
                                                ###############Euró
                                                if(q == "e"):
                                                    txt="\tIrjon be egy új árat: "
                                                    ujar=int(input(txt))/300
                                                    lista[e][f+1]= ujar
                                                    print("\tKész")
                                                    #print(lista)
                                                    c = 1
                                                    o=1

                                                ###################Ft
                                                elif(q == "f"):
                                                    txt="\tIrjon be egy új árat: "
                                                    ujar=input(txt)
                                                    lista[e][f+1]=ujar
                                                    print("\tKész")
                                                    #print(lista)
                                                    c = 1
                                                    o=1

                                                elif(q == "vissza"):
                                                    c = 1

                                                else:
                                                    txt="\tNem értem\n" ###egyéb eset, még egy if es ág sem futott le 
                                                    print(txt)
                    


                                        if (name  == "vissza"):
                                            o=1
                                            c=0
                            
                            if(c != 1 and o !=1 ):
                               print("\tNem értem\n")
                   
                    
##############################################################################                    
                    
                    elif(d=="vissza"):     
                        x=6            
                                                    #"mit szeretnél modosítani"
                    else: 
                        txt2= "\tNem értem"
                        print(txt2)

                    if(c == 1 or o==1):
                            ff= open(nev_1, "w")
                            for i, e in enumerate(lista):
                                for m, k in enumerate(e):
                                    if(k == e[0]):
                                        ff.write(str(k)+ ";" )
                                    else:
                                        ff.write(str(k)+ "\n")
                            ff.close()


            ##################################################################
                   
            else:
                txt="\tNincs ilyen fájl név"         
                print(txt)

            ################################################################# Ár nincs módodsítva 

#modositas()
    




