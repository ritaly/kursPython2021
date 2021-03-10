poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem = poem.lower()
poem = poem.replace(',', '')
poem = poem.split()

poem_dict = {}

for word in poem:
    if word in poem_dict:
        poem_dict[word] += 1
    else:
        poem_dict[word] = 1

for key, value in poem_dict.items():
    print(key, ':', value)