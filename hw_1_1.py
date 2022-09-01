#question 01

import datetime
current = datetime.datetime.now()
date = "{}/{}/{}".format(current.day,current.month,current.year)
time = "{}:{}:{}".format(current.hour,current.minute,current.second)
print("Current date and time: ")
print(date)
print(time)