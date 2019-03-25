#today's date in format: Monday, January 10th 2019 at 1:15pm”.

#use datetime
import datetime

day = datetime.datetime.today()

print(day.strftime("%A, %B %Dth %Y at %I:%M%p"))