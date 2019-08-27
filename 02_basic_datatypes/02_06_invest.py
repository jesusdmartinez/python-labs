'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

dollas = input("how much you wanna spend?")
interest = input("whats the rate g?")
years = input("how much time u got")
print(int(dollas) * (1 + int(interest)) ** int(years))
