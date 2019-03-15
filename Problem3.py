#print numbers between 1000 and 10000 divisible by 6 but not 12

#create range
nums = range(1000,10000)

#use modulo
for n in nums:
    if n % 6: 
        continue
    elif not(n % 12):
        continue
    else:
        print(n)