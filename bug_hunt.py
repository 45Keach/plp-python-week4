count = 1
total = 0

# BUG: The while statement was missing a colon, so I added one.
# BUG: The condition stopped at 4 because it used < 5, so I changed it to <= 5 to include 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Python cannot concatenate a string and an integer directly, so I changed this to use a comma.
print("Sum of 1 to 5 is:", total)
