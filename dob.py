from datetime import datetime
from dateutil import relativedelta

first = datetime(1999,10,3)
second = datetime(2023,7,7)
difference = relativedelta.relativedelta(second,first)
print(difference.years, difference.months, difference.days)
diff = (second - first).days
print(diff)

thisday = datetime.today()
print(thisday)

 