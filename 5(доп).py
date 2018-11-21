import random
n = int(input("Введите количесвто бросков: "))
amount2 = 0
amount1 = 0

while n>0:
    raz = random.randint(1,2)
    if raz == 1:
        #Орел
        amount1 += 1
    else:
        #Решка
        amount2 += 1
    n -= 1
print(amount1, " раз выпал 'Орел'")
print(amount2, " раз выпал 'Решка'")
input("Введите Enter , чтобы закончить.")
