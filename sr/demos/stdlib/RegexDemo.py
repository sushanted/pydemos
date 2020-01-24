import re

# Find
print(re.findall('\\d+', "There are 7 days in 1 week, 365 days in 1 year"))

# Replace
print(re.sub('(\\d+)', '<\\1>', "There are 7 days in 1 week, 365 days in 1 year"))

# Special regex symbol : r : specifies that it is a regex, so we don't have to escape \ (as in above examples)
# our regex becomes more readable

print(re.findall(r'\d+', "There are 7 days in 1 week, 365 days in 1 year"))
print(re.sub(r'(\d+)', r'<\1>', "There are 7 days in 1 week, 365 days in 1 year"))

# Already compiled pattern
compiled = re.compile(r'\d+')
print("Found matches by compiled pattern: ", compiled.findall("There are 7 days in 1 week, 365 days in 1 year"))

# Accessing groups
compiled_date = re.compile(r'(?P<day>\w{3}) (?P<month>\w{3}) (?P<date>\d+) (?P<time>.+) (?P<ampm>PM|AM)')

# This is like matcher in Java
search_result = compiled_date.search("Fri Jan 24 6:34:16 PM")

if search_result:
    print("Groups as dictionary:", search_result.groupdict())
    print("Second group:", search_result.group(2))
    print("First and Third groups:", search_result.group(1, 3))
    print("Time group:", search_result.group("time"))
    print("Time groups:", search_result.group("time", "ampm"))
    (day, date) = search_result.group('day', 'date')
    print("Day and date:", day, date)

# Match vs Search : match exactly matches from start of the string, search matches any occurrence of the regex
print("Match: ", re.match(r'\d', "e34"))
print("Search: ", re.search(r'\d', "e34"))
