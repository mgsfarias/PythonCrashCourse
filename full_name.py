#Using variables in strings - f strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #For variables in strings insert f before "
print(full_name.title())

print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)