#Using variables in strings - f strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #For variables in strings insert f before "
print(full_name.title())

print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

print("\tPython") # use \t for tab before string
print("Languages: \nPython \nC \nJavaScript") #use \n for line break
print("Languages: \n\tPython \n\tC \n\tJavascript") #use case tab and line break

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)