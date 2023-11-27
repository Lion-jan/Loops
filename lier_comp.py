import random

input_numbers=[]
son = random.randint(0,3)
failed = True

for i in range(5):
    print('adashdingiz bu biz oylagan son emas')
    print('')
    print(f"sizda {5-i} ta imkoniyat bor")
    print('')
    user_son = int(input("o'ylangan sonni taxmin qiling=>"))
    if user_son == son:
        print('siz yutdingiz')
        input_numbers.append(user_son)
        print(input_numbers)
        failed=False
        break
    else:
        input_numbers.append(user_son)


else:
    print('siz yutqazdingiz endi tamomsiz ')
    print(input_numbers)
    print(f"biz o'ylagan son {son} edi")