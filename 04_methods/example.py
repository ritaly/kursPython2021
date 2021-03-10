def ask_about_mood():
    question = 'How are you?'
    print(question)


def show(user_response):
    print('^^^', user_response, '^^^')

# main part of the code
print('*********')
ask_about_mood()

response = input('--> answer here: ')
show(response)
print('-----END----')

