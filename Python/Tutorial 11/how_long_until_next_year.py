from datetime import datetime
today = datetime.now()
print("The current date is", today)
year = today.year
print(year)
next_year = year +1
print(next_year)
new_year = "1-1-"+str(next_year)+"-0:00:00"
print(new_year)
new_year_date = datetime.strptime(new_year,"%m-%d-%Y-%H:%M:%S")
print(new_year_date)
time_remaining = new_year_date-today
print(time_remaining)