import datetime
import time
import pytz

to_day = datetime.datetime.today()
print("Current Date and time :|:", to_day)
print("Current Date and time :|:", datetime.datetime.now())
print("Current Date :|:", to_day.date())
print("Today's Date :|:", to_day.day)
print("Current Month :|:", to_day.month)
print("Current Year :|:", to_day.date().year)
print("Week of the day :|:", to_day.date().isoweekday())
print("Date 5 days back :|:", datetime.date.today() - datetime.timedelta(days=5))
print("Date 5 days after :|:", datetime.datetime.now() + datetime.timedelta(days=5))
print("Seconds remaining in my coming BDay :|:", (datetime.datetime(year=2021, month=10, day=4, hour=0, minute=0) - to_day).seconds)
print("Seconds consumed in running this program :|:", (datetime.datetime.now() - to_day).microseconds)
print("Current Time :|:", to_day.time())
print("Current Time minute", datetime.datetime.now().time().minute)
print("Current Time hour", datetime.datetime.now().time().minute)
print("Current Time seconds", datetime.datetime.now().time().second)
print("Current Time microseconds", to_day.time().microsecond)


print("Current Epoch time\t", time.time(), "Seconds")
print("Current Epoch time\t", time.time_ns(), "Nanoseconds")

utc_dt = datetime.datetime(2021, 10, 4, 12, 44, 56, 10, tzinfo=pytz.utc)
print("Time Zone aware date time\t", utc_dt)

current_utc_dt = datetime.datetime.now(tz=pytz.utc)
print("Current UTC Time Zone\t", current_utc_dt)

current_utc_dt = datetime.datetime.now(tz=pytz.utc)
print("Convert UTC to India Time zone \t", current_utc_dt.astimezone(tz=pytz.timezone("Asia/Calcutta")))

curr_dt = datetime.datetime.today()
print("Naive time to timezone aware \t", curr_dt, pytz.timezone("Asia/Calcutta").localize(curr_dt))
print("ISO format \t", curr_dt.isoformat())
