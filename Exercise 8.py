# the list of names
names = ["jake", "zac", "ian", "ron", "sam", "dave"]

# asks the user to search a name
search = input("Search for someone: ").strip().lower()

# Search for the name in the list
if search in names:
    print(f"{search} is on the list!")
else:
    print(f"{search} is not on the list.")
