# Practical 6 - Fuzzy Logic
# Union, Intersection and Complement

# CHANGE VALUES HERE
A = {"x1": 0.5, "x2": 0.7, "x3": 0.0}
B = {"x1": 0.8, "x2": 0.2, "x3": 1.0}

# If the question gives a third set, uncomment this:
# C = {"x1": 0.6, "x2": 0.4, "x3": 0.9}

# PUT THE SETS HERE
# For 2 sets:
sets = [A, B]

# For 3 sets, use:
# sets = [A, B, C]

# UNION = MAXIMUM membership value
union = {}
for key in A:
    values = [s[key] for s in sets]
    union[key] = max(values)

# INTERSECTION = MINIMUM membership value
intersection = {}
for key in A:
    values = [s[key] for s in sets]
    intersection[key] = min(values)

# COMPLEMENT OF A = 1 - membership value
complement_A = {}
for key in A:
    complement_A[key] = 1 - A[key]

# OUTPUT
print("Set A:", A)
print("Set B:", B)

if len(sets) == 3:
    print("Set C:", C)

print("\nUnion:", union)
print("Intersection:", intersection)
print("Complement of A:", complement_A)
