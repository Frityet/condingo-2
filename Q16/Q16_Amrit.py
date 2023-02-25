# Uncomment the code below and fix the bug as described in the question.
# Underneath the fixed code, describe what the initial issue was and how
# you fixed it.

# This was read, when it should have been write
file = open("new_file.txt", "w")
name = input("Please enter a first name: ")
file.write(name)
# The file closed here
age = input("Please enter a last name: ")
file.write(age)
file.close()

