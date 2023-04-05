import datetime
import timedelta

x = datetime.datetime.today()
print(x)

y = datetime.date.today()
formatted_date = y.strftime("%a %d %B %Y")
print("date " ,y)
print("formatted date ", formatted_date)

pcn_date = input("Whats the PSN date in the following format DDMMYYYY: ")
date_obj = datetime.datetime.strptime(pcn_date, '%d%m%Y')
print(date_obj)
duration = timedelta.Timedelta(days = 14, weeks=1)
deadline = date_obj + duration
print(deadline)
formatted_deadline = deadline.date().strftime("%d %b %Y")
print("\n If you pay PCN until {}, you will have to pay 65$".format(formatted_deadline))

