#program to check first letter of the day of the week

#use datetime
import datetime

#set variable for today
day = datetime.datetime.today().strftime('%A')

#check and print
if  day[0] == "T":
  print("Today is", day, ", which starts with a 'T'.")

else:
  print("Today is", day, ", which does not start with 'T'.")