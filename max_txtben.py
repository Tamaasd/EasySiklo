
import os
összes_file=os.listdir()



def inputFile_as_string(file, lista):
    f= open(file , "r" )
    for sor in f:
        sor= sor[:-1].split(";") 
        lista.append([str(sor[0]), int(sor[1])] )
    f.close()
    return




def txt_legnagyobb():
    r=1
    while(r==1):
        lista= [["a",0]]
        file_adatok=[]
        q=0
        f=0
        u=1
        összes_file = os.listdir()
        nemtalált_file=1
        file_találat=0
        txt="\n\tKérek egy fájl nevet:"
        nev_1=input(txt)+".txt"

        if (nev_1 == "vissza.txt"):
            r=0
        else:
        
            összes_file = os.listdir()

            for file_1 in összes_file:
                
                if file_1 == nev_1 :
                    file_találat=2
        ##########################################################################ha többszőr kéri be az adatot, az azért van , mert a pl input(txt) több változóhoz van egyszerre hozzárendelve 
            if file_találat == 2:           #ha megtalálta
                
                inputFile_as_string( nev_1, file_adatok) 

            for e , fájlok_litsái in enumerate (file_adatok):

                for r, adatok in enumerate(fájlok_litsái):

                    if (adatok == fájlok_litsái[1]):
                        a= int(adatok)

                        for j, lista_lista in enumerate (lista):
                            #print(lista_lista)

                            for t, lista_elemek in enumerate (lista_lista):    
                                #print(lista_elemek)

                                if(lista_elemek == lista_lista[1] and lista_elemek<adatok):
                                    #print(file_adatok[e])
                                    lista=[file_adatok[e]]
                                    u=0
  #############################################################################################                               
    
            if(file_találat==0):
                print("\tNincs ilyen fájl")
                q=1
################################################################################################            
            if u==0 and q==0 :
                x=1
                while(x==1):
                    txt2="\tForint vagy Euro?[f/e]:"
                    pénz=input(txt2)
                    if(pénz=="f"):
                        print("\n\tA legnagyobb elem: ", lista[0][0] , "-", lista[0][1], "Forint")
                        x=0
                    elif(pénz=="e"):
                        eu=int(lista[0][1])/300
                        print("\t\nA legnagyobb elem: ", lista[0][0] , "-", eu , "Euro")
                        x=0                
                    elif(pénz=="vissza"):
                        x=0

                    else:
                        print("\tNem értem\n")       

#txt_legnagyobb()