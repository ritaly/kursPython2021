fopen = open('tekst.txt', 'r')
print("I'm open")
print(fopen)
raise Exception("I'm rebel!'")
fopen.close() # nie wykona się
print('The end')