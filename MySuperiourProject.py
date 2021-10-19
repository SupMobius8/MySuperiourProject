print("Hello, user!")
ik=""
while len(ik)!=11 or ik.isdigit()!=True:
    try:
        ik=input("Введи IDkood => ")
    except ValueError:
        print("Ошибка!")
print("IDkood анализ:".center(50,"-"))
print("Первый символ:")
ik_list=list(ik)
if int(ik_list[0]) not in [1,2,3,4,5,6]:
    print(ik_list[0]," - не правильно!")
else:
    print(ik_list[0]," - правильное число!")
    kuu=ik_list[3]+ik_list[4]
    kuu=int(kuu)
    if kuu>0 and kuu<13:
        print(ik_list[3]+ik_list[4]," - данные правильные, ваш месяц рождения!")
    else:
        print(ik_list[3]+ik_list[4]," - не правильные данные!")
    päev=ik_list[5]+ik_list[6]
    päev=int(päev)
    if päev>0 and päev<32:
        print(ik_list[5]+ik_list[6]," - данные правильные, ваш день рождения!")
    else:
        print(ik_list[5]+ik_list[6]," - не правильные данные!") 
    if int(ik_list[0])==1 or int(ik_list[0])==2:
        aasta=int("18"+ik_list[1]+ik_list[2])
    elif int(ik_list[0])==3 or int(ik_list[0])==4:
        aasta=int("19"+ik_list[1]+ik_list[2])
    elif int(ik_list[0])==5 or int(ik_list[0])==6:
        aasta=int("20"+ik_list[1]+ik_list[2])
    print(aasta," - ваш год рождения!")
    if int(ik_list[0])==1 or int(ik_list[0])==3 or int(ik_list[0])==5:       
        m="Mees"
        print("Ваш пол - ", m)
    elif int(ik_list[0])==2 or int(ik_list[0])==4 or int(ik_list[0])==6:
        n="Naine"
        print("Ваш пол - ",n)
Summa=0
for i in range(1,11):
    if i<10:
        Summa+=i*int(ik_list[i-1])
    else:
        Summa+=(i-9)*int(ik_list[i-1])
print("Summa: ",Summa)
остаток=Summa//11
if остаток==10:
    Summa=0
    for i in range(3,13):
        if i<=9:
            Summa+=i*int(ik_list[i-1])
        else:
            Summa+=(i-9)*int(ik_list[i-1])
    остаток=Summa//11
остаток=Summa-остаток*11
print("Контрольное число - ", остаток)
ikoodid=[]
arvud=[]
if остаток==int(ik_list[10]):
    print("IDkood правильный!")
    ikoodid.append(ik)
else:
    print("IDkood неправильный!")
    arvud.append(ik)
    

