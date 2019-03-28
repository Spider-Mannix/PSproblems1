#print numbers between 1000 and 10000 divisible by 6 but not 12

#create range
nums = range(1000,10000)

#use modulus operator
for n in nums:
    #check division of 6
    if n % 6: 
        continue
    #check division of 12    
    elif not(n % 12):
        continue
    else:
        print(n)