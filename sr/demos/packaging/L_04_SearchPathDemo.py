import sys

# search order
# 1. first find build in
# 2. find all dirs mentioned in sys.path

# sys.path inclusion
# 1. directory from which the script is run
# 2. PYTHONPATH shell variable

print("sys.path= ",sys.path)

# sys path can be modified programtically
sys.path.append("/Users/sravale/Personal/Repos/more")

print("sys.path= ",sys.path)