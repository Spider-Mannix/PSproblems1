#successive calculation down to value of 1

x = int(input("Please input a postive integer: "))

while x > 1:
    if x % 2:
        x = (x*3) + 1
    else: 
        #not(x % 2):
        x = x/2
    print(x)
print(x)

#put in failsafes
