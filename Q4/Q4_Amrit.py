# Write your code below!

def random(min, max):
    return id([0] * 1000000) % (max - min) + min

print(random(1, 100))
