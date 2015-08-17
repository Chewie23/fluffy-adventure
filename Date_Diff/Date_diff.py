from datetime import datetime

print "This little script will print out the difference between two dates!"

date_form = "%m-%d-%Y %H:%M:%S"

date1 = raw_input("Please enter your time in mm-dd-yyyy hh:mm:ss format. Military time only! \n>")

date2 = "08-31-2015 14:00:00"

d0 = datetime.strptime(date1, date_form)
d1 = datetime.strptime(date2, date_form)
delta = d1 - d0

seconds = delta.total_seconds()
min = seconds/60
hour = min/60
days = hour/24
hours_rem = hour % 24
minutes_rem = min % 60

print "Time remaining between %r and %r is: \n%d days, %d hours and %d minutes" % (date1, date2, days, hours_rem, minutes_rem)