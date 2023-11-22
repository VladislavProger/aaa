import random


def igra():
    cumma = random.randint(4, 30)
    print(f"-----------\nВ кучке {cumma} камней\nВы можете брать 1, 2 или 3 камня\n"
          f"Победил тот, кто взял последний камень\n-----------")
    while cumma > 0:
        if cumma < 4:
            bot = cumma
        else:
            bot = random.randint(1, 3)
        cumma -= bot
        print(f"Компьютер выбрал {bot}. Осталось камней: {cumma}\n")
        if cumma <= 0:
            print("К сожалению, вы проиграли!\n")
            break
        while True:
            try:
                Ya = int(input("Ваш ход: "))
            except ValueError:
                print('Необходимо ввести число от 1 до 3\n')
                continue
            if Ya < 1 or Ya > 3:
                print("Необходимо взять от 1 до 3 камней.\n")
            elif Ya > cumma:
                print("В кучке недостаточно камней. Попробуйте ещё раз.\n")
            else:
                cumma -= Ya
                print(f"Осталось камней: {cumma}\n")
                break
        if cumma <= 0:
            print("Вы выиграли\n")
            break
    igra()


igra()
