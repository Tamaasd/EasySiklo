
import os
összes_file=os.listdir()


def inputFile_as_string(file, lista):
    f= open(file , "r" )
    for sor in f:
        sor= sor[:-1].split(";") 
        lista.append([str(sor[0]), int(sor[1])] )
    f.close()
    return




def keresés_minden_fájlban():
    
    r=1
    while r==1:
        lista=[]
        f=0
        g=0
        u=1
        összes_file = os.listdir()
        txt = "\n\tKérek egy nevet:"
        name=input(txt)


        for k, file in enumerate (összes_file):    #keresünk az összes fájlban 


            if(file[-4:] == ".txt"):   # ha txt 
                
                lista=[]   #lista törlése minden új txt inputolása elött
                
                inputFile_as_string(file,lista) #az első fájt betesszük a listába

                for a, elem_listák in enumerate (lista):  #keresük a fáj listájában 
                    #print(elem_listák)
                    
                    for b, elemek in enumerate  (elem_listák): # keresünk a fájl listájának listájiban 
                        #print(elemek)

                        
                        if (elemek == name ):
                            while ( u==1):
                                txt="\tForint vagy Euro? [f/e]:"
                                pénz=input(txt)
                                if (pénz == "f"):
                                    print("\t\nAz elem a/az " ,összes_file[k] ,"-ben található:" )
                                    print("\t",elem_listák[b], "-" , str(elem_listák[b+1]) ,"Forint")
                                    u=0
                                
                                elif(pénz == "e"):
                                    print("\t\nAz elem a/az " ,összes_file[k] ,"-ben található:" )
                                    print("\t",elem_listák[b], "-" , str( int(elem_listák[b+1]) /300 ) , "Euro")
                                    u=0

                                elif(pénz == "vissza"):
                                    u=0  
                                
                                else:
                                    print("\tNem értem\n")
                            
                            g = 1

            else:
                txt1="\tNincs ilyen"


        if(name== "vissza"):
            r=0
        
        elif(g<1):
            print(txt1)

#keresés_minden_fájlban()                          





