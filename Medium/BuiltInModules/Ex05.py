import datetime

print(datetime.datetime.now())

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

date_string = "2024-05-08"
print(datetime.datetime.strptime(date_string, "%Y-%m-%d"))

date1 = datetime.datetime(2024, 5, 8)
date2 = datetime.datetime(2024, 5, 10)
date_difference = date2 - date1  # Difference between date2 and date1
print("Difference between two dates:", date_difference)

print(datetime.date.today().strftime("%Y-%m-%d"))

timedelta = datetime.timedelta(days=7)
print(datetime.datetime.now() + timedelta)

print(datetime.datetime.now().strftime("%A"))