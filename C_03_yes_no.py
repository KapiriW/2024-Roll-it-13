
while True:

    try:
my_num = int(input("enter an integer"))
print("your number is ", my_num)

    except ValueError:
        print("please enter an integer")