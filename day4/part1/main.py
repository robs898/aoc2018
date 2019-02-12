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
        sleep_duration = int(wake_time) - int(sleep_time)
        if guard_id in sleep_minutes:
            sleep_minutes[guard_id] += range(int(sleep_time), int(wake_time))
        else:
            sleep_minutes[guard_id] = range(int(sleep_time), int(wake_time))

# find sleepiest guard
longest_sleep_time = 0
for guard_id in sleep_minutes:
    if len(sleep_minutes[guard_id]) > longest_sleep_time:
        longest_sleep_time = len(sleep_minutes[guard_id])

for guard_id, sleep_time in sleep_minutes.items():
    if len(sleep_time) == longest_sleep_time:
        sleepiest_guard = guard_id

# find sleepiest minute
sleepiest_minute = 0
for minute in set(sleep_minutes[sleepiest_guard]):
    if sleep_minutes[sleepiest_guard].count(minute) > sleep_minutes[sleepiest_guard].count(sleepiest_minute):
        sleepiest_minute = minute

print(int(sleepiest_guard) * int(sleepiest_minute))
