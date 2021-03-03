people = [
    ["Dorota", "Wellman", "dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["Robert", "Lewandowski", "piłkarz"],
    ["Krystyna", "Janda", "aktorka"]
]
counter = len(people)

for index in range(counter):
    print(index + 1, ' - '.join(people[index]))

print('------------')

for row in people:
    print(row[0], row[1], '-', row[2])

