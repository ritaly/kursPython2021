def ask_about_mood():
    question = 'How are you?'
    print(question)


def show(user_response):
    print('^^^', user_response, '^^^')


def multiply_sentence(counter):
    sentence = "I love Python!"
    return sentence * counter

# main part of the code
print('*********')
ask_about_mood()

response = input('--> answer here: ')
show(response)

exclamation = multiply_sentence(5)
print(exclamation)
print('-----END----')

