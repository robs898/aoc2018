import re


# get patterns from input
sleep_minutes = {}

for line in open('input_sorted.txt'):
    s = line.strip()
    guard_line = re.match(r'.*Guard #(\d+) begins shift', s)
    sleep_line = re.match(r'.+:([0-9]{2})] falls asleep', s)
    wake_line = re.match(r'.+:([0-9]{2})] wakes up', s)
    if guard_line:
        guard_id = guard_line.group(1)
    if sleep_line:
        sleep_time = sleep_line.group(1)
    if wake_line:
        wake_time = wake_line.group(1)
        for minute in range(int(sleep_time), int(wake_time)):
            if guard_id in sleep_minutes:
                if str(minute) in sleep_minutes[guard_id]:
                    sleep_minutes[guard_id][str(minute)] += 1
                else:
                    sleep_minutes[guard_id][str(minute)] = 1
            else:
                sleep_minutes[guard_id] = {}

largest_count = 0
for guard_id, minute_counts in sleep_minutes.items():
    for minute, count in minute_counts.items():
        if count > largest_count:
            largest_count = count
            frequent_minute = minute
            frequent_guard = guard_id

print(int(frequent_minute) * int(frequent_guard))
