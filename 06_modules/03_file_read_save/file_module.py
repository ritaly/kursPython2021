def read_file(filename):
    text = '***'
    try:
        with open(filename) as file:
            text = file.read()
    except FileNotFoundError:
        return 'file not found error'

    if text == '':
        return 'file is empty'

    return text


def save_file(filename, content):
    try:
        with open(filename, 'x', encoding='UTF-8') as file:
            file.write(content)
    except FileExistsError:
        return 'not saved, file already exist'

    return 'file successfully saved'

