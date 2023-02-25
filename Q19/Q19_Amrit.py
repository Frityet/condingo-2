# Write your code here!
# Your code must give results for word counts on all
# three sample texts given to get full points.
import sys

with open(sys.argv[1], 'r') as f:
    text = f.read()
    i = 0
    for word in text.split():
        i += 1
    print(i)
