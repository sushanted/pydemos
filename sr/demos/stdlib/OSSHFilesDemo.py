import os, shutil, glob

# Can land into any directory
print("CWD:", os.getcwd())
os.chdir("..")
print(f"Directories in {os.getcwd()} \n")

# Any OS specific command can be executed
print(os.system("ls"))

# shutil has more file/dir related methods
print(shutil.disk_usage(os.getcwd()))
print(shutil.which("ls"))

# This similar to ant style file listing
print(*(file + "\n" for file in glob.glob(os.getcwd() + "/**/__init__.py", recursive=True)))
# Note : *iterable : unpacks the iterable into the evaluated values
