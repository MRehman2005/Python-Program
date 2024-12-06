# Read the input
n = int(input())  # number of elements in the tuple
elements = map(int, input().split())  # space-separated integers

# Create the tuple
t = tuple(elements)

# Compute the hash of the tuple
print(hash(t))
