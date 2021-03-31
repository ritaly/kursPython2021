import file_module as fm

if __name__ == '__main__':
    print(fm.read_file('test.txt'))

    text_to_save = 'Lalalalal'
    print(fm.save_file('save.txt', text_to_save))