from datetime import datetime, date, timedelta

period=365
print(datetime.today())
print(timedelta(days=period))

print(datetime.today()-timedelta(days=period))
