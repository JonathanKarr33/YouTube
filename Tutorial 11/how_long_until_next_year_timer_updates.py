from datetime import datetime
from time import sleep
today = datetime.now()
print("The current date is", today)
year = today.year
next_year = year +1
new_year = "1-1-"+str(next_year)+"-0:00:00"
while(year<next_year):
    new_year_date = datetime.strptime(new_year,"%m-%d-%Y-%H:%M:%S")
    time_remaining = new_year_date-today
    print(time_remaining, end="\r")
    sleep(1)
    today = datetime.now()
print("Happy Near Year!")