
import os
lista=[]


def törlés():
    h = 1
    while h==1:
        lista=[]
        ll=0
        kk=0
        txt="\n\tÍrd be a fájl nevét:"
        file=input(txt)+".txt"
        li = os.listdir()
        for i in li:
            if i == file :
                kk=1
            else:
                ll=1
        if kk == ll:

            
            inputFile_as_string(file, lista)
            #print(lista)
            x = 0
            while x != 1:
                
                m = 0
                n = 0
                c = 0
                while c == 0:
                    item = input("\tÍrd be a törölni kívánt elemet: ")           
                    for e, i in enumerate(lista):
                        for l, t in enumerate(i): 
                            if (t == item):
                       
                                biztos = input("\tBiztosan törölni szeretnéd? [i/n]")
                                if "i" == biztos:                           
                                    c = 1                            
                                    lista.pop(e)                                                           
                                    m = 1
        
                                if biztos == "n":
                                    c = 0
                                    m = 1

                                else:
                                    n = 1

                            if (m >=n ):
                                ff= open(file, "w")
                                for i, q in enumerate(lista):
                                    for ba, k in enumerate(q):
                                        if(k == q[0]):
                                            ff.write(str(k)+ ";" )
                                        else:
                                            ff.write(str(k)+ "\n")
                                            
                            if (item == "vissza"):
                                x = 1
                                m = 1
                                c = 1

                            else:
                                n = 1

                    if m != 1 and n <= 1:                                                                                                                                   
                        print("\tNincs ilyen elem, próbáld újra!\n")
                        
        elif( file == "vissza.txt"):
            h = 0

        else:
            print("\tNincs ilyen fájl")



def inputFile_as_string(file, lista):
    f = open(file, "r")
    for sor in f:
        sor=sor[:-1].split(";")
        lista.append([str(sor[0]), int(sor[1])])
    f.close()


#main
törlés()