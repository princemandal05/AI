# Practical 5: Alpha-Beta Pruning Algorithm
# Ready-to-run Python program
#
# To use different values, edit the "value" tuple below.
# The values can be large or small, positive or negative.
# For a complete binary game tree, use 2, 4, 8, 16, 32, ... leaf values.

import math


def alphabeta(depth, index, is_max, value, alpha, beta, max_depth):
    # Base condition: return the leaf value
    if depth == max_depth:
        return value[index]

    # Maximizing player
    if is_max:
        best = -math.inf

        for i in [0, 1]:
            val = alphabeta(
                depth + 1, index * 2 + i, False,
                value, alpha, beta, max_depth
            )

            best = max(best, val)
            alpha = max(alpha, best)

            # Prune branches that cannot affect the result
            if beta <= alpha:
                print("Pruned at Max node", index)
                break

        return best

    # Minimizing player
    else:
        best = math.inf

        for i in [0, 1]:
            val = alphabeta(
                depth + 1, index * 2 + i, True,
                value, alpha, beta, max_depth
            )

            best = min(best, val)
            beta = min(beta, best)

            # Prune branches that cannot affect the result
            if beta <= alpha:
                print("Pruned at Min node", index)
                break

        return best


# Change these leaf values for your question.
value = (3, 5, 6, 9, 1, 2, 0, -1)


def main():
    # Check that the number of values is 2, 4, 8, 16, ...
    if len(value) < 2 or (len(value) & (len(value) - 1)) != 0:
        print("Error: Use 2, 4, 8, 16, 32, ... leaf values.")
        print("Current number of values:", len(value))
        return

    max_depth = int(math.log2(len(value)))

    optimal_value = alphabeta(
        0, 0, True, value,
        -math.inf, math.inf, max_depth
    )

    print("Leaf values:", value)
    print("Optimal Value:", optimal_value)


if __name__ == "__main__":
    main()
