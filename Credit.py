c = "Y"


def checksum(num):
    check = 0
    s1 = 0
    s2 = 0

    while (num != 0):
        d = num % 10
        check += 1
        if check % 2 == 1:
            s1 += d
        else:
            d = 2*d

            while d != 0:
                r = d % 10
                s2 += r
                d //= 10
        num //= 10
    sum = s1 + s2
    if sum % 10 == 0:
        return 0
    else:
        return 1
        

while c == "Y":
    print()
    num = int(input("Enter Card Number: "))
    result = checksum(num)
    if (result == 0):
        two_digit = num // (10**13)
        if (two_digit == 34) or (two_digit == 37):
            card = "American Express"
        elif (two_digit // 10 >= 51) and (two_digit // 10 <= 55):
            card = "Mastercard"
        elif (two_digit // 100 == 4):
            card = "VISA"
        else:
            card = "Invalid"
    else:
        card = "Invalid"
    
    
    print(f"Your card is {card}.")
    print()
    c = input("Try another Card Number? (y/n) -> ").upper()


