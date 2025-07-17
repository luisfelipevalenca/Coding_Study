import datetime
now = datetime.datetime.now()

print(now)

formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)

# >> 2025-07-17 16:04:57.428184
# >> 2025-07-17 16:04:57
