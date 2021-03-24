with open('save.txt', 'w') as f:
    f.write('Line 1')
    f.write('Line 2\n')
    f.write('Line 3')
    f.write('Line 4\n')

    sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']
    f.write('\n'.join(sweets_list))

