

def game():

    # bu qiziq masalani baribir ishlashim kerak


    kataklar = [1, 2, 3, 4, 5, 6, 7, 8, 9]



    def show_status():
        print(f"            {kataklar[0]}|{kataklar[1]}|{kataklar[2]}")
        print('            - - -')
        print(f"            {kataklar[3]}|{kataklar[4]}|{kataklar[5]}")
        print('            - - -')
        print(f"            {kataklar[6]}|{kataklar[7]}|{kataklar[8]}")

    def who_win():
        if kataklar[0] == kataklar[4] == kataklar[8] or kataklar[2] == kataklar[4] == kataklar[6]:

            return True
        elif kataklar[0] == kataklar[3] == kataklar[6] or kataklar[1] == kataklar[4] == kataklar[7] or kataklar[2] == \
                kataklar[5] == kataklar[8]:

            return True
        elif kataklar[0] == kataklar[1] == kataklar[2] or kataklar[3] == kataklar[4] == kataklar[5] or kataklar[6] == \
                kataklar[7] == kataklar[8]:

            return True

    game_limit = True

    isX = True

    is0 = True

    while game_limit:
        show_status()

        while isX:
            a = int(input(' 0 kiriting '))
            if (kataklar[a - 1] != 'X') and kataklar[a - 1] != '0':
                kataklar[a - 1] = '0'
                show_status()
                who_win()
                if (who_win()):
                    print(' 0 lar yutdi. tabriklaymiz')
                    want = str(input("yana o'ynashni xoxlaysizmi y(ha) n(yoq)"))
                    if want =='y':
                        game()
                    elif want == 'n':
                        game_limit = False
                        break
                isX = False
                is0 = True
            else:
                print("bu katak bo'sh emas qaytadan kiriting")
                continue

        while is0:
            b = int(input('X kiriting '))
            if kataklar[b - 1] != '0' and kataklar[b - 1] != 'X':
                kataklar[b - 1] = 'X'
                who_win()
                if (who_win()):
                    print(' 0 lar yutdi. tabriklaymiz')
                    want = str(input("yana o'ynashni xoxlaysizmi y(ha) n(yoq)"))
                    if want == 'y':
                        game()
                    elif want == 'n':
                        game_limit = False
                        break
                isX = True
                is0 = False
            else:
                print("bu katak bo'sh emas qaytadan kiriting")



game()



