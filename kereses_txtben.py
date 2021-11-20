
import os
összes_file=os.listdir()


def inputFile_as_string(file, lista):
    f= open(file , "r" )
    for sor in f:
        sor= sor[:-1].split(";") 
        lista.append([str(sor[0]), int(sor[1])] )
    f.close()
    return




def keresés_txt():
    r=1
    while(r==1):
        lista=[]
        f=2
        g=1
        u=1

        összes_file = os.listdir()

        nemtalált_file=1
        file_találat=0
        txt="\n\tIrjon be egy fájl nevet: "
        nev_1=input(txt)+".txt"

        if (nev_1 == "vissza.txt"):
            r=0
        else:
        
            összes_file = os.listdir()

            for file_1 in összes_file:
                
                if file_1 == nev_1 :
                    file_találat=2
                
        
            if file_találat == 2:
                while(g==1):
                    txt = "\tIrjon be egy nevet: "                               
                    name=input(txt)
                
                    inputFile_as_string( nev_1, lista)
                

                    for a, elem_listák in enumerate (lista): 
                                        
                                        
                        for b, elemek in enumerate  (elem_listák): 
                            

                            
                            if (elemek == name ):
                                while ( u==1):
                                    txt="\tForint vagy Euro? [f/e]: "
                                    pénz=input(txt)
                                    if (pénz == "f"):
                                        print("\n\t" , elem_listák[b], "-" , str(elem_listák[b+1]) ,"Forint")
                                        u=0
                                    
                                    elif(pénz == "e"):
                                        print("\n\t", elem_listák[b], "-" , str( int(elem_listák[b+1]) /300 ) , "Euro")
                                        u=0

                                    elif(pénz == "vissza"):
                                        u=0
                                    
                                    
                                    else:
                                        print("\tNem értem\n")
                                
                                g = 0

                            elif(name== "vissza") :
                                u = 0 
                                g=0
                        

                            else:
                                f=1
                    if(f==u):
                        print("\tNincs ilyen név\n")

            else:
                print("\tNincs ilyen fájl")

#keresés_txt()
            
       
           


                
            





