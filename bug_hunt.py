count = 1
total = 0

# BUG: The while statement was missing a colon, so I added one.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Python cannot concatenate a string and an integer directly, so I changed this to use a comma.
print("Sum of 1 to 5 is:", total)
