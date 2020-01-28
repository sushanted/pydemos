# both single and double quotes work for strings

print("inside double")

print('inside single')

print("'single' inside \"double\"")

print('"double" inside \'single\'')

# \ has special meaning
print("old\tline\nnew\tline\"quoted\"")

# escaped \
print("old\\tline\\nnew\\tline")

# r : raw text : \ has no special meaning : printed as is : even the escape is also printed
print(r"old\tline\nnew\tline\"quoted\"")

# multiline
print(""" This can span
MANY
multiple lines""")

# multiline string : escaped newline characters
print(""" This can span \
MANY \
multiple lines""")

# concatenation
print("way" + '1')
print("way" '2' " works with only literals not variables")

# multiply
print("_" * 100)

# indexing

print("\nindexing demos\n")

word = "01234";

print("word[3]=", word[3])
# print("last char=",last char)
print("word[-1]=", word[-1])
# print("range : include first index, exclude second index=",range : include first index, exclude second index)
print("word[1:3]=", word[1:3])
# print("till n (excluding n)=",till n (excluding n))
print("word[:3]=", word[:3])
# print("from n (including n)=",from n (including n))
print("word[3:]=", word[3:])
# complete word
print("word[:3]+word[3:]=", word[:3] + word[3:])

# This will cause an error : index is too large
# print("word[2000]=",word[2000])

# This will NOT cause an error : handled by python properly
print("word[2:2000]=", word[2:2000])

# strings are immutable : following won't work
# word[3] = '9'
# word[2:3] = '10'

# length
print("length", len(word))

# formatting
print("\nFormatting\n")
name = 'Tom'
age = 44.234

# Variable interpolation
print(f'{name} is {age} years old')

# Logger kind format
print("{} is {:8.4} years old".format(name, age))  # 8 chars with spaces, total 4 digits
print("{1} is the  age of {0}".format(name, age))

# String modulo operator: this is like printf but it is an operation in string and not related to the print function
print("number %9.3f" % (3.42))  # 9 chars including spaces, 3 digits
print("number %2.3f" % (123.42395))  # 9 chars including spaces, 3 digits

# 0: padd the value with 0 #: print the 0x, x:convert it to hex, 9: print 7 chars including zeros(or spaces) before
print("number in hex %0#9x" % 345)  # 0x0000159

# Separate values with a space and append full stop after the last value.
print("A", "simple", "sentence", sep=' ', end='.')
