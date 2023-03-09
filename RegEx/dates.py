import re

text = input()

pattern = r'\b(?P<day>\d{2})(?P<sep>[-./])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})\b'

result = re.finditer(pattern,text)

for el in result:
    current_date = el.groupdict()

    print(f'Day: {current_date["day"]}, Month: {current_date["month"]}, Year: {current_date["year"]}')
