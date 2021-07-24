from datetime import datetime, timedelta
current_date = datetime.now()
print("Today: " + str(current_date))
one_day = timedelta(days=1)
yesterday = current_date - one_day
print("Yesterday: " + str(yesterday))
favorite_date = "03/20/4032"
favorite_date = datetime.strptime(favorite_date,"%m/%d/%Y")
print(favorite_date)
print("Month: " + str(favorite_date.month))
print(favorite_date.strftime("%A, %B %d, %Y"))
time1 = "11:43:02"
time2 = "11:56:01"
time1 = datetime.strptime(time1,"%H:%M:%S")
time2 = datetime.strptime(time2,"%H:%M:%S")
print(time2 - time1)