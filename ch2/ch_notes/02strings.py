#These are all safe to be used as a string value
string_1='I told my friend, "Python is my favorite language!"'
string_2="The language 'Python' is named after Monty Python, not the snake."
string_3="One of Python's strengths is its diverse and supportive community."

print(string_1)
print(string_2)
print(string_3)

name = 'ada lovelace'
name_1= 'ADA LOVELACE'
print(name.title())
print(name.upper())
print(name_1.lower())       # Most useful once, everytime we take user-input
                            # we will use this method.
first_name = 'ada'
last_name = 'lovelace'

full_name = f"{first_name.title()} {last_name.title()}"
print("Her full name is:",full_name)

print("Hello, " f"{full_name.title()}!")

print("Line without tab")
print("\t Line with tab")

print("Line without new line")
print("\n Line with new line")

print("\n\t Line with new line and tab!")

var_with_rspace = "python "
var_with_lspace = " python"
var_with_space= " python "

print(var_with_rspace.rstrip())
print(var_with_rspace.lstrip())
print(var_with_space.strip())

url = "https://googlyboogly.com"
print(url.removeprefix('https://'))
