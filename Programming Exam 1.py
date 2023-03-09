#TrungDong
#U42594715
#input 2 number for numerator and denominator. Program ouput if the fraction is proper or improper 
#if improper than ouput a mixed number 


import math
a = int(input("Enter a numerator: Value must be greater than 0: "))

while a <= 0:
    try:
        a = int(input("Please re-enter the numerator. Value must be greater than 0: "))
        if a <= 0:
            raise ValueError
        else:
            break
    except ValueError:
        continue

b = int(input("Enter a denominator: Value must be greater than 0: "))

while b <= 0:
    try:
        b = int(input("Please re-enter the denominator. Value must be greater than 0: "))
        if b <= 0:
            raise ValueError
        else:
            break
    except ValueError:
        continue


gcd = math.gcd(a,b)

if a < b:
    print(f"{a}/{b} is a proper fraction.")
    if gcd != 1:
        a = a // gcd
        b = b // gcd
        print(f"This proper fraction can be reduced to: {int(a):.0f} / {int(b):.0f}")
    else:
        print("This proper fraction cannot be reduced any further.")

else:
    print(f"{a}/{b} is an improper fraction.")
    if gcd != 1:
        a = a // gcd
        b = b // gcd
        print(f"This improper fraction can be reduced to: {int(a):.0f} / {int(b):.0f}")
        mixed_number = f"{int(a // b)} and {int(a % b)} / {b}"
        if int(a % b) == 0:
            print(f"The whole number is {int(a // b)}")
        else:
            print("The mixed number is " + mixed_number)
    else:
        print("This improper fraction cannot be reduced any further.")
        
        mixed_number = f"{int(a // b)} and {int(a % b)} / {b}"
        if int(a % b) == 0:
            print(f"The whole number is {int(a // b)}")
        else:
            print("The mixed number is " + mixed_number)
        
