# Try to print the day, month, year in the form “Today is 03/10/2023”.
import datetime

date = datetime.datetime.now()
formated_date = date.strftime("%d/%m/%Y")

print("Date:", formated_date)