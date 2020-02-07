import os, re

path = '/Users/sravale/Personal/Repos/pydemos/sr/demos/OO'
start_from = 5

file_regex = re.compile(r'L_(\d+)_(.+)')

for search_result in (file_regex.search(name) for name in os.listdir(path)):
    if search_result and int(search_result.group(1)) >= start_from:
        os.chdir(path)
        os.rename(search_result.group(0), f'L_%0#2d_%s' % (int(search_result.group(1)) + 1, search_result.group(2)))
