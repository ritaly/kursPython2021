def hello():
    name = 'powitanie' # scope/kontekst

    def good_morning(counter): # funkcja lokalną
        return name * counter

    return good_morning


welcome_fun = hello() # good_morning
print(welcome_fun(4))

