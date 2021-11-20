import os
összes_file=os.listdir()


def inputFile_as_string(file, lista):
    f= open(file , "r" )
    for sor in f:
        sor= sor[:-1].split(";") 
        lista.append([str(sor[0]), int(sor[1])] )
    f.close()
    return

def atlag_txt():
    
   
    r=1
    while(r==1):
        u=1
        file_adatok=[]
        lista= []
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


        
                inputFile_as_string( nev_1 , file_adatok) 

                for e , fájlok_litsái in enumerate (file_adatok):

                        for r, adatok in enumerate(fájlok_litsái):

                            if (adatok == fájlok_litsái[1]):
                                a= int(adatok)
                                
                                lista.append(adatok)
                                #print(lista)
                                #print(sum(lista))
                                u=0

                                
        if u==0 :
            x=1
            while(x==1):
                txt2="\n\tFt vagy Euro?[f/e]: "
                pénz=input(txt2)
                if(pénz=="f"):
                    atlag=sum(lista) / len(lista)
                    #print(atlag)
                    print("\n\tÁtlag:",atlag, "Forint"  )
                    x=0
                
                elif(pénz=="e"):
                    euatlag=(sum(lista)/len(lista))/300
                    print("\n\tÁtlag: ",euatlag , "Euro" )
                    x=0                
                elif(pénz=="vissza"):
                    x=0

                else:
                    print("\tNem értem")    

        else:
            print("\tNincs ilyen fájl")   

#atlag_txt()