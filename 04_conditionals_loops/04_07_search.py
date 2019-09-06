'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

num = 1
user_num = 0
while not int(user_num) in range(1,1000):
    user_num = input("tell me a number between 0 and 1,000")

while num in range(1,1000):
    if num == int(user_num):
        break
    print(num)
    num += 1
print("your number is " + user_num)
