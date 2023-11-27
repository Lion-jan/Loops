import random


def nimadir(a):
    if a%2==0:
        return 'juft'
    else:
        return 'toq'

list_length  = int(input('massiv uzunligini kiriting ='))

juft_sonlar =[]
toq_sonlar  =[]


# newList = []
#
# for i in range(0,list_length):
#     a =random.randint(0,10000)
#     newList.append(a)
#
#
#
# for i in newList:
#     print(f"{i}-{nimadir(i)} son")


# raxmat aka dastur zo'r ishladi mana sizga 5000$ 😊😊😊



#  bu masalaning 2-usuli




for i in range (0,list_length):
    a = random.randint(0, 10000)
    if nimadir(a)=='juft':
        juft_sonlar.append(a)
    else:
        toq_sonlar.append(a)

print(toq_sonlar,juft_sonlar)