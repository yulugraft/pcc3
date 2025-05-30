name = "eric"
message = f"Hello, {name.title()} would you like to learn some Python today?"
print(message)

# syntax of f-strings
# TODO

first_name = "eric"
last_name = "matthes"

full_name_titlecase = f"{first_name.title()} {last_name.title()}" 
print("Full-name in Title Case:", full_name_titlecase)

full_name_lowercase = f"{first_name} {last_name}"
print("Full-name in lowercase:", full_name_lowercase)

full_name_UPPER = f"{first_name.upper()} {last_name.upper()}"
print("Full-name in UPPERCASE:", full_name_UPPER)

quote = "D.H. Lawrence once remarked, 'Perhaps you're a slave to your own idea\
 of yourself'. "         # The \ in the previous line is a line-break
print(quote)

famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new"

print(famous_person, "once said,", f"'{quote}.'")

name_with_space = "\t hello \nthere!"
print("Name with weird whitespace:", name_with_space)
print("lstrip():", name_with_space.lstrip())
print("rstrip():", name_with_space.rstrip())
print("strip():", name_with_space.strip()) # So strip() does not work on \n?!?!

filename = 'python_file.txt'
print("The file name (without the suffix) is: ", filename.removesuffix('.txt'))

print("######################################################################")

#  2-9 Number Eight
print(4 + 4)
print(12 - 4)
print(4 * 2)
print(32 / 4)

# 2-10 Favourite Number
fav_num = 5
print("My favourite number is:", fav_num)

print("######################################################################")

# 2-11 Comments
#  This is nice program that writes my name in the console!
print("MY NAME HAHAHAHAHAHA!")

print("######################################################################")

# 2-12 Zen of Python  by Tim Peters
import this
