rate1 = int(input('Podaj ocene 1-10: '))
rate2 = int(input('Podaj ocene 1-10: '))
rate3 = int(input('Podaj ocene 1-10: '))

if (rate1 + rate2 + rate3)/3 >= 7:
    print("bardzo dobry")
elif (rate1 + rate2 + rate3)/3 >= 5:
    print("przecietna")
else:
    print("nie warta uwagi")

