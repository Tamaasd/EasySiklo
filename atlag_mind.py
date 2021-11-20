import os
összes_file=os.listdir()


def inputFile_as_string(file, lista):
    f= open(file , "r" )
    for sor in f:
        sor= sor[:-1].split(";") 
        lista.append([str(sor[0]), int(sor[1])] )
    f.close()
    return

def atlag_mindenben():
    u=1
    file_adatok=[]
    lista= []
   
    összes_file = os.listdir()

    for b, file in enumerate (összes_file):

        if(file[-4:] == ".txt"): 
        
            inputFile_as_string( file , file_adatok) 

            for e , fájlok_litsái in enumerate (file_adatok):

                    for r, adatok in enumerate(fájlok_litsái):

                        if (adatok == fájlok_litsái[1]):
                                              
                            lista.append(adatok)
                            
                            u=0
            file_adatok=[]
            #print(lista)
                            
    if u==0 :
        x=1
        while(x==1):
            txt2="\n\tFt/Euró?[f/e]:"
            pénz=input(txt2)
            if(pénz=="f"):
                atlag=sum(lista)/len(lista)
                #print(atlag)
                print("\n\tÁtlag:",atlag, "Forint\n"  )
                x=0
            elif(pénz=="e"):
                euatlag=sum(lista)/len(lista)/300
                print("\n\tÁtlag: ",euatlag , "Euro\n" )
                x=0                
            elif(pénz=="vissza"):
                x=0

            else:
                print("\tNem értem")      
