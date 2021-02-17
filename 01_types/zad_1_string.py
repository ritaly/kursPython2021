# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
# i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

txt = 'abrakadabra'
middle = len(txt)//2
element = txt[middle] # a
prev = txt[middle-1] # k
next = txt[middle+1] # d

print(prev + element + next)

# string[start : stop]
print(txt[middle-1:middle+2])

