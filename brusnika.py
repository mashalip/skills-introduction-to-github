"""Это программа для расчёта пропорций, если кол-во одного ингредиента изменится"""

print('брусника маринованная')

brusnika_marin = {"brusnika" : 300, "sugar" : 100, "salt" : 120, "water" : 100}
print(brusnika_marin)

if __name__ == '__main__':
    delitel = 1

    for ingridient, weit in brusnika_marin.items():
        print(ingridient, weit)

        quantity = input()
        if quantity == "":
            continue

        quantity = int(quantity)

        if  quantity == 0 or quantity == weit:
            continue

        else:
        #if quantity != weit:
            delitel = weit / quantity
            print(delitel)
            break

    for ingridient, weit in brusnika_marin.items():
        weit /= delitel
        print(ingridient, weit)



















