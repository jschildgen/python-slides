from datetime import datetime, timedelta

a = datetime(2027, 5, 31)
b = datetime(2026, 5, 31)
c = datetime(2027, 5, 31, 15, 30, 59, 999999)
jetzt = datetime.now()

print(a.year)       # 2027

diff = a - b
print(diff.days)    # 365

d = a + timedelta(days=5, hours=12)
print(d)            # 2027-06-05 12:00:00