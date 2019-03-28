#successive calculation down to value of 1 using input number

#request number
x = int(input("Please input a postive integer: "))

#insert conditions
while x > 1:

    #check if odd
    if x % 2:
        x = (x*3) + 1

    #if even   
    else: 
        x = x/2
    print(x)
print(x)