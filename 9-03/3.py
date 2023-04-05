import datetime
import timedelta

dt = datetime.datetime.now()
print(dt)

timestamp = dt.strftime("%Y%m%d%_%H%M%S%f")

print("timestamp ", timestamp)