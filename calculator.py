import time
# The mining of import is something is called
print("my name is Abdulla.\nI use python to write it.\nwellcome to use it")
print("if you want add click S.\nif you want subtract click S\nif you want to multiply click X\nif you want to divide click D")

choice = input("\wich letter?\n").upper()

numberX = int(input("write the first number: "))
# The numberX is variable
numberY = int(input("write the seconds number"))

multiply = "X"
add = "A"
subtract = "S"
divide = "D"


if choice == add:
    answer = numberX + numberY
    print(answer)
elif choice == subtract:
    answer = numberX - numberY
    print(answer)
elif choice == multiply:
    answer = numberX * numberY
    print(answer)
elif choice == divide:
    answer = numberX / numberY
    print(answer)
else:
    print("use the intruction above")


print("plese wait for 5.....seconds")



time.sleep(5)