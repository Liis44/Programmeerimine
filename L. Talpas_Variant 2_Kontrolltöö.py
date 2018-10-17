'''Variant 2'''

'''Ülesanne 1'''


#Ülesandest valesti aru saadud!
'''def elements_sum(N):
    # alustuseks oletame, et N=0
    theSum = 0
    for i in N:
    # liidame järjendile otsa järgmise arvu
        theSum = theSum + i
    # liidab kokku kõik numbrid ja tagastab vastuse
    return theSum'''

#Mina oleks lahendanud seda ül niimoodi:
#funktsioon võtab sisend täisarvu N ja annab vastuseks numbrite 1 kuni N summa
def elements_sum(N):
    #kõige pealt kasutan N-i absoluutväärtust (nt. -5, muudab 5ks)
    from math import fabs
    N=fabs(N)
    tulemus=0
    # kasutan stüklit. Võtab arvu, lahutab ühe ja liidab eelmise arvuga. Kuni 0ni
    while N>=0:
        tulemus=tulemus+N
        N=N-1
    return tulemus
        
    
print(elements_sum(-5))




'''Ülesanne 2'''

'''def time_convert(time_string):
    # alustuseks oletame, et meil on null minutit, kuna kellaaeg 00:00 on sisuliselt 0 minutit
    minutes= 0
    # jagame kellaaja kaheks osaks ('part') funktsiooniga .split
    for part in time_string.split(':'):
    # leiame kellaaja minutites korrutades esimese osa ('part'), mis on tunnid, 60'ga (kuna ühes tunnis on 60 minutit). Seejärel liidame saadud tulemusele otsa kellaaja teise osa ('part'), mis juba on minutites ning saame kellaaja minutites kokku.
        minutes = minutes*60 + int(part)
    return minutes

print(time_convert('13:37'))'''

'''Ülesanne 3'''

'''def sort_values(string):
    for i in string.split(','):
        list_sorted = sorted([i for i in string if str(i).isdigit()]) + sorted([i for i in string if not str(i).isdigit()])
    return list_sorted
print(sort_values(str("2,a,54,v,y,8")))'''

'''# Kuna ei saanud 3.-ndat ülesannet funktsioonina tööle, siis proovisin teha niisama nagu allpool ja siis töötas:
sort_values=str("2,a,54,v,y,8")
# Jagan ära stringi juppideks
list = sort_values.split(',')
# Sorteerin stringi selliselt, et ta kõigepealt leiaks ülesse numbrid listist...
list_sorted_1 = sorted([i for i in list if str(i).isdigit()])
# ... ja seejärel leiaks ülesse tähed listist
list_sorted_2 = sorted([i for i in list if not str(i).isdigit()])
# numbrite ja tähede vahel on "new line" element (uus rida), mille tegemiseks olen printinud listid eraldi. Saaks kuidagi kasutada ka kombinatsiooni \n.
print(list_sorted_1)
print(list_sorted_2)'''
