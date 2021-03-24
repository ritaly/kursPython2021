filename = 'tekst.txt'

with open(filename, 'r') as file:
    content = file.readlines()

print("-------------------")

# for index in range(len(content)):
#     print(f"{index} -> {content[index]}")

for index, line in enumerate(content):
    print(index, '-->', line)