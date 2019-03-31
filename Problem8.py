#today's date in format: Monday, January 10th 2019 at 1:15pm.

#use datetime
import datetime

#take today's date
day = datetime.datetime.today()

#format as required using strftime
print(day.strftime("%A, %B %dth %Y at %I:%M%p"))