
import os

összes_file=os.listdir()


def inputFile_as_string(file, lista):
    f= open(file , "r" )
    for sor in f:
        sor= sor[:-1].split(";") 
        lista.append([str(sor[0]), int(sor[1])] )
    f.close()
    return

def min_mindenben():
    u=1
    file_adatok=[]
    lista= [["a",100000000000000000]]
   
    összes_file = os.listdir()

    for b, file in enumerate (összes_file):

        if(file[-4:] == ".txt"): 
        
            inputFile_as_string( file , file_adatok) 

            for e , fájlok_litsái in enumerate (file_adatok):

                    for r, adatok in enumerate(fájlok_litsái):

                        if (adatok == fájlok_litsái[1]):
                            a= int(adatok)

                            for j, lista_lista in enumerate (lista):
                                #print(lista_lista)

                                for t, lista_elemek in enumerate (lista_lista):    
                                    #print(lista_elemek)

                                    if(lista_elemek == lista_lista[1] and lista_elemek>adatok):
                                        #print(file_adatok[e])
                                        lista=[file_adatok[e]]
                                        u=0
                                        filename=összes_file[b]
    if u==0 :
        x=1
        while(x==1):
            txt2="\n\tForint vagy Euro?[f/e]:"
            pénz=input(txt2)
            if(pénz=="f"):
                print("\n\tA legkisebb elem: ", lista[0][0] , "-", lista[0][1], "Forint -a/az", filename , "-ben\n" )
                x=0
            elif(pénz=="e"):
                eu=int(lista[0][1])/300
                print("\n\tA legkisebb elem: ", lista[0][0] , "-", eu , "Euro  -a/az", filename , "-ben\n" )
                x=0                
            elif(pénz=="vissza"):
                x=0

            else:
                print("\tNem értem")       

#min_mindenben()


        


