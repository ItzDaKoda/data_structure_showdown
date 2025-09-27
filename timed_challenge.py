# Problem 7: First Repeated Value
# Return the first value that repeats in the collection.
# Input: [1, 4, 3, 5, 3, 2, 1]
# Output: 3

def first_repeated_value(values):
    seen = set()
    for v in values:
        if v in seen:
            return v
        seen.add(v)
    return None  # No repeats found

# --- Tests ---
print(first_repeated_value([1, 4, 3, 5, 3, 2, 1]))  # 3
print(first_repeated_value([10, 20, 30, 40]))       # None
print(first_repeated_value([]))                     # None
print(first_repeated_value([7, 7, 7]))              # 7
