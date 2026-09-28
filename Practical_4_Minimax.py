# Practical 4: Minimax Algorithm
# Ready-to-run Python program
#
# To use different values, edit the values list below.
# IMPORTANT: The number of values must be 2, 4, 8, 16, ... (a power of 2).
# The values themselves can be small or large, positive or negative.

import math

# Leaf-node values (change these as needed)
values = [2, 3, 5, 9]


def minimax(depth, node_index, is_max, values, max_depth):
    """Return the Minimax value for the current node."""

    # Base case: reached a leaf node
    if depth == max_depth:
        return values[node_index]

    # MAX player chooses the larger child value
    if is_max:
        left_value = minimax(
            depth + 1, node_index * 2, False, values, max_depth
        )
        right_value = minimax(
            depth + 1, node_index * 2 + 1, False, values, max_depth
        )
        return max(left_value, right_value)

    # MIN player chooses the smaller child value
    else:
        left_value = minimax(
            depth + 1, node_index * 2, True, values, max_depth
        )
        right_value = minimax(
            depth + 1, node_index * 2 + 1, True, values, max_depth
        )
        return min(left_value, right_value)


def main():
    if not values:
        print("Error: Please add values to the values list.")
        return

    # A complete binary game tree needs a power-of-2 number of leaf values.
    if len(values) & (len(values) - 1):
        print("Error: The number of values must be 2, 4, 8, 16, ...")
        print("You currently have", len(values), "values.")
        return

    max_depth = int(math.log2(len(values)))
    result = minimax(0, 0, True, values, max_depth)

    print("Leaf values:", values)
    print("Maximum depth:", max_depth)
    print("Minimax result:", result)


if __name__ == "__main__":
    main()
