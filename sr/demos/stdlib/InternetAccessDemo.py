from urllib.request import urlopen
import re

country_name_regex = re.compile(r'\s+[A-Z]{3,}\s(\w+)')

with urlopen("http://web.stanford.edu/~chadj/shcodes.txt") as query_result:
    for line in query_result:
        line = line.decode('utf-8')
        country_name = country_name_regex.search(line)
        if (country_name):
            print(country_name.group(1))
