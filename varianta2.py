def read_list():
    lista=[]
    nr=int(input("Cate numere doriti: "))
    for i in range(nr):
        lista.append(int(input("dati al {}-lea numar: ".format(i + 1))))
    return lista

def numere_prime(nr):
    # int=nr
    #output=True or False in functie daca nr e prim sau nu
    #verificam daca numarul are divizori in afara de el insusi sau de 1 excluzandu i pe acestia
    #daca nr este prim return True daca se gaseste un divizor imediat este returnat false
    k=0
    if nr==0 or nr==1:
        return False
    if nr==2 or nr==3:
        return True
    i=2
    while nr>i:
        if nr%i==0:
            k=1
            return False
        i=i+1
    if k==0:
        return True

def ultimele_3_cifre_numar(nr):
    #restul impartirii cu 1000 ne ofera ultimele 3 cifre ale unui nr
    nr=nr%1000
    return nr


def lista_ultimele_cifre(lista):
    #verificam fiecare termen prin comparatie cu un temp care tot timpul ia valoarea lui lista[i]si verifica daca e mai mare decat rezultatul pana in acel moment
    temp=0
    rezultat=0
    x=0
    for i in range(len(lista)):
        x=ultimele_3_cifre_numar(lista[i])
        if numere_prime(x)==True:
            temp=lista[i]
        if temp>rezultat:
            rezultat=temp
    return rezultat

def verificare_rezultat():
    assert(lista_ultimele_cifre([1234, 456,890,23]))==23
verificare_rezultat()

def palindrom(nr):
    #verificam daca un numar poate sa fie scris invers prin intoarcerea sa intr o alta variabia
    m = nr
    a=0
    while nr!=0:
        a=a*10+nr%10
        nr=nr//10
    if m==a:
        return True
    else:
        return False

def suma_cifre(nr):
    #il dezmembram pe nr impartindu l cu 10 ,iar restul impartirii sale cu 10 ne da fiecare cifra care o adunam ins
    n=nr
    s=0
    while n>0:
        s=s+n%10
        n=n/10
    return s

def lista_sume(lista):
    #int:lista
    #output:t
    #i am dat lui rezultat o valoare mare astfel incat sa ne fie usor sa comparam, iar mai apoi am salvat in w suma cifrelor
    #am verificat daca e palindrom si am comparat o cu rezultat, in cazul in care era mai mica i am atribuit lui t lista[i]
    rezultat=9999
    temp=0
    w=0
    for i in range(len(lista)):
        w=suma_cifre(lista[i])
        if palindrom(w)==True:
            temp=lista[i]
            if temp<rezultat:
                rezultat=temp
    if rezultat==9999:
        return("nu exista")
    return rezultat



def verificare_lista2():
    assert lista_sume([56,7771,23,45])==23
verificare_lista2()

def lista_patrat(lista):
    #luam o lista goala rezultat si prin doua for-uri parcurgem lista, daca lista[i]*lista[i]==lista[j] rezulta avem un patrat in lista si il introducem in lista
    rezultat=[]
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i]!=1:
                if lista[i]*lista[i]==lista[j]:
                    rezultat.append(lista[j])
    return rezultat

def verificare_lista3():
    assert(lista_patrat([3,4,9,16,5,12,25]))==[9,16,25]
    assert(lista_patrat([1,1,23,46,55,77,3,9,4,16]))==[9,16]
verificare_lista3()

def logarithm(nr):

    import math

def lista_proprietate5(lista,w):
    #folosind functiile matematice log(x,base a) si sqrt care e radical putem sa gasim radicalul si logartimult cu input de baza
    #le salvam in 2 variabile care mai apoi le introducem intr o mini lista in cadrul listei mari si o returnam
    import math
    rezultat=[]
    x=0
    q=0
    for i in range(len(lista)):
        x=float(math.sqrt(lista[i]))
        q=float(math.log(lista[i],w))
        rezultat.append([x,q])
    return rezultat

def verificare_lista5():
    assert lista_proprietate5([9,81],3)==[[3.0,2.0],[9.0,4.0]]
    assert lista_proprietate5([4,16,64],2)==[[2.0,2.0],[4.0,4.0],[8.0,6.0]]
verificare_lista5()


def show_menu():
    print("1.Citire Lista: ")
    print("2.Afisare numere cu proprietate 2: ")
    print("3.Afisare numere cu proprietate 3: ")
    print("4.Afisare numere cu proprietatea 4: ")
    print("5.Afisare numere cu proprieattea 5: ")
    print("x.Iesire ")

def interface():
        lista = []
        while True:
            show_menu()
            op = input("Optiune: ")
            if op == "1":
                lista =read_list()
            elif op == "2":
                print(lista_ultimele_cifre(lista))
            elif op == "3":
                print(lista_sume(lista))
            elif op == "4":
                print(lista_patrat(lista))
            elif op == "5":
                w=int(input("baza este: "))
                print(lista_proprietate5(lista,w))
            elif op == "x":
                break
            else:
                print("invalid")
interface()











