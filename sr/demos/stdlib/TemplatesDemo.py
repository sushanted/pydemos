from string import Template

template = Template("User ${name} has $action machine $ip")

print(template.substitute(dict(name='Ashok', action='Logged in', ip='10.0.0.1')))

print(template.substitute(dict(name='Prashant', action='Logged off', ip='10.0.0.2')))


# Custom template with custom delimiter
class CustomTemplate(Template):
    delimiter = '%'


customTemplate = CustomTemplate("%d %m %y")

print(customTemplate.substitute(dict(d=24, m=1, y=2020)))

# safe : we can miss some args with safe_substitute
print(customTemplate.safe_substitute(dict(y=90, m=9)))
