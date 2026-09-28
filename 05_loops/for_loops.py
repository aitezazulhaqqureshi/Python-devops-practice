# Basic for loop
for x in range(5):
    print(x)

# Print Hello World 5 times
for x in range(5):
    print("Hello World")

# Range from 10 to 49
for x in range(10, 50):
    print(x)

# Even numbers from 2 to 20
for x in range(2, 21, 2):
    print(x)

# Backward counting
for x in range(20, 1, -2):
    print(x)

# Server status check
for x in range(1, 11):
    if x % 3 == 0:
        print("Server", x, ": WARNING")
    else:
        print("Server", x, ": ONLINE")