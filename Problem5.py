#check if a number is prime

#a prime number is divisible only by itself and 1 - use modulus?

x = int(input("Please input a postive integer: "))

#iterate between 1 and x and check modulus
i = 1
while i <= x:
    i += 1
    if x % i:
        continue 
    elif x == i and not(x % i):
        print(x, "is a prime number")  
    else:
        print(x, "is not prime")
        break
