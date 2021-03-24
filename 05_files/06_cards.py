def can_be_card_number(user_input):
    if not len(user_input) in [13, 15, 16]:
        return False

    if not user_input.isdigit():
        return False

    return True


def is_visa(card_number):
    if card_number[0] == '4' and len(card_number) in [13, 16]:
        return True
    else:
        return False


def is_mastercard(card_number):
    # numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
    if (51 <= int(card_number[0:2]) <= 55 or 2221 <= int(card_number[0:4]) <= 2720) and len(card_number) == 16:
        return True
    else:
        return False


def is_american_express(card_number):
    if card_number[0:2] in ['34', '37'] and len(card_number) == 15:
        return True
    else:
        return False


def read_cards_number(filename) -> list:
    with open(filename) as fp:
        content = fp.readlines()
    return content


def save_cards_number(filename, card_number):
    with open(filename, 'a') as fp:
        fp.write(card_number + '\n')

# main code

cards_list = read_cards_number('cards.txt')

for card in cards_list:
    card = card.replace(' ', '').strip()
    if can_be_card_number(card):
        if is_visa(card):
            print('Visa card')
            save_cards_number('visa.txt', card)
        elif is_mastercard(card):
            print('MasterCard')
            save_cards_number('mastercard.txt', card)
        elif is_american_express(card):
            print('American Express')
            save_cards_number('americaexpress.txt', card)
        else:
            print('Inna karta')
            save_cards_number('other.txt', card)
    else:
        print('This input is not a card number')
