'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''

def webby(func):
    def wrapper(text):
        initial = func(text)
        new = f"<p>{initial}</p>"
        return new
    return wrapper

@webby
def enter_text(text):
    return text

print(enter_text('yo'))
