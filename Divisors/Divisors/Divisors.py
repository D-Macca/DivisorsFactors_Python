__author__ = "Darcy MacCuspie"
again = "y"
import time


def Divisor_Test():
    num = int(input("Please input a number to find out its divisors: "))
    potential_divisors = list(range(1,num+1))
    divisors = []
    for number in potential_divisors:
        progress = float((number/num)*100)
        print(("%.2f"  % progress) + "% complete")
        if num % number == 0:
            divisors.append(number)


    print(divisors)
while again == 'y':
    Divisor_Test()
    again = input("Run again? y/n >>>")
    if again != "y":
        print("Goodbye")
        time.sleep(3)