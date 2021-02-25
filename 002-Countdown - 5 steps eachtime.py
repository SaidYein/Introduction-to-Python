number = int(input("enter an integer"))

while number > 0:
    if number%5 ==0:
        go = input("Do you wanna continue y/n?")
        if go == "n":
            print("Countdown stopped")
            break
    print(number)
    number - = 1
else:
    print("Continue here...")