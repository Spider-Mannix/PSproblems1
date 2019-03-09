# ask for number 

while True:
    try:
        x = int(input("Please input a postive integer: "))
        #check if positive 
        if x <= 0:
            print("We're looking for a whole number greater than 0")
            x = int(input("Please input a postive integer: "))
            if x > 0:
                break   
            break
    except ValueError:
        print("We're looking for a whole number greater than 0")

# "\n"

#create variables
ans = 0
i = 1

# from lecture video:
while i <= x:
    ans = ans + i
    i = i + 1

print("The sum of all integers between 1 and {} (inclusive) is: ".format(x), ans)