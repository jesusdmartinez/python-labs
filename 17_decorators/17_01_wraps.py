'''
Write a decorator function that wraps text passed to it in a html <p> tag.

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



# def webby(func):
#   def wrapper(text):
#     initial_result = func(text)
#     new_result = f"<p>{initial_result}</p>"
#     return new_result
#   return wrapper
#
# @webby
# def say_something(text):
#   return text
#
# print(say_something("HEI WHAT'S UP?"))





