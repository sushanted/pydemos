import os

tmp_file = "../tmp/file"
tmp_binary_file = "../tmp/bin_file"

# open file in writing mode
with open(tmp_file, "w") as writable_file:
    writable_file.write("header:\n")
    writable_file.writelines([f"line{i}\n" for i in range(1, 4)])
# with closes the file when going out of scope (This is similar to try(resource) in java)

# open file in reading mode (r is optional)
with open(tmp_file) as readable_file:
    # read entire file
    print("Entire file once: ", readable_file.read())

with open(tmp_file) as readable_file:
    # read limited chars
    print(readable_file.read(8))
    print(readable_file.read(5))

with open(tmp_file) as readable_file:
    # read line by line
    print(f"first line: {readable_file.readline()}")
    print(f"second line: {readable_file.readline()}")

# File is an iterable, so all operators are applicable
print("Iterating through complete file:")
with open(tmp_file) as readable_file:
    for line in readable_file:
        print(line)

with open(tmp_file) as readable_file:
    print("All lines as a list:", readable_file.readlines())

with open(tmp_file) as readable_file:
    print("All lines as a list:", list(readable_file))

with open(tmp_file) as readable_file:
    print("line contains in the file: ", "line1\n" in readable_file)

os.remove(tmp_file)

print("\nBinary Mode\n")

# Create the file (somehow rb+ not creating the file)
with open(tmp_binary_file, "w") as binary_file:
    pass

with open(tmp_binary_file, "rb+") as binary_file:
    print("Position before write:", binary_file.tell())
    binary_file.write(b's123456789')
    # tell the current position in the file
    print("Position after write:", binary_file.tell())
    # Go to the start of the file and write there
    binary_file.seek(0)
    binary_file.write(b'0')
    binary_file.seek(0)
    print("Content of file after write:", binary_file.read(10))
    binary_file.seek(3)
    print("Third and fourth chars:", binary_file.read(2))
    # skip 2 from current position (whence:1): chars 5 and 6
    binary_file.seek(2, 1)
    print("Seventh and eighth chars:", binary_file.read(2))
    # Read 2 bytes in above call, now rewind by 2 again
    binary_file.seek(-2, 1)
    print("Again Seventh and eighth chars:", binary_file.read(2))
    # Now start from the end and rewind 5 chars
    binary_file.seek(-5, 2)
    print("Last five chars:", binary_file.read(10))
os.remove(tmp_binary_file)
# open file in reading and writing mode
# f= open("file","r+")
