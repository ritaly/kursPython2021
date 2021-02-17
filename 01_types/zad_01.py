# Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.

mileage_per_100 = 6.4
distance = 120
cost = 5.04

total = distance/100 * mileage_per_100 * cost

print("Koszt wyprawy to:", round(total,2) )
