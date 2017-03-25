import sys

time = input().strip()

splitted = time.split(':')

hours_12 = int(splitted[0])
mins = splitted[1]
secs = splitted[2][:2]

is_pm = splitted[2].endswith("PM")

if (is_pm):
    if (hours_12 >= 1 and hours_12 < 12):  # between 1pm and 11:59pm
        hours_12 += 12
else:
    if (hours_12 == 12):
        hours_12 -= 12

print(':'.join(list((str(hours_12).zfill(2), mins, secs))))
