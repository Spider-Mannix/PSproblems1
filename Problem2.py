#checking commit
#use datetime
import datetime

#set variable
day = datetime.datetime.today().weekday()

#check and print
if  day == 1:
  print("Today is Tuesday, which starts with a 'T'.")

elif day == 3:
  print("Today is Thursday, which starts with a 'T'.")

else:
  print("Today does not start with 'T'.")