import time

year, month, day = time.strftime("%Y-%m-%d").split("-")
print('{}/{}/{}'.format(day,month,year))
