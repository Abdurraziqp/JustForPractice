minute =int(input('Enter minute:\n'))
hours = minute // 60
minute_remaining = minute % 60

print(minute, 'minute(s) is', hours, 'hours and', minute_remaining, 'minutes.')
