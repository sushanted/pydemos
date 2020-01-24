from datetime import date

print(date.today())

birth_day = date(1986, 10, 15)
print(birth_day)

# Calendar arithmetic
age = date.today() - birth_day;

print("Age in days", age.days)

# Formatting
print(date.today().strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
