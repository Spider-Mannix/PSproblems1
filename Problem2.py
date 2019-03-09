#program to check first letter of the day of the week

#use datetime
import datetime

#set variable for today
day = datetime.datetime.today().strftime('%A')

#comma as string to tidy whitespace
comma =","

#check and print
if  day[0] == "T":
  print("Today is", day + comma, " which starts with a 'T'.")

else:
  print("Today is", day + comma, " which does not start with 'T'.")

