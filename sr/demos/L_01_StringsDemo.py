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

#concatenation
print("way"+'1')
print("way" '2' " works with only literals not variables")

#multiply
print("_"*100)

#indexing

print("\nindexing demos\n")

word = "01234";

print("word[3]=",word[3])
# print("last char=",last char)
print("word[-1]=",word[-1])
# print("range : include first index, exclude second index=",range : include first index, exclude second index)
print("word[1:3]=",word[1:3])
# print("till n (excluding n)=",till n (excluding n))
print("word[:3]=",word[:3])
# print("from n (including n)=",from n (including n))
print("word[3:]=",word[3:])
# complete word
print("word[:3]+word[3:]=",word[:3]+word[3:])

# This will cause an error : index is too large
#print("word[2000]=",word[2000])

# This will NOT cause an error : handled by python properly
print("word[2:2000]=",word[2:2000])

#strings are immutable : following won't work
#word[3] = '9'
#word[2:3] = '10'

#length
print("length",len(word))




