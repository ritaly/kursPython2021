# Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
# Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
# Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie
# np. “Mój pies, rasy border collie wabi się Dyzio”

animal = ('pies', 'kundelek', 'Figa')
type_of_animal, race, name = animal
sentence = f"Mój { type_of_animal }, rasy { race } wabi się  { name }"
print(sentence)