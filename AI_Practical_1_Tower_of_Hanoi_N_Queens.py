# AI Practical 1
# Tower of Hanoi and N-Queens Problem

# 1. Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)


print("===== TOWER OF HANOI =====")
num_discs = int(input("Enter number of disks: "))
tower_of_hanoi(num_discs, 'A', 'B', 'C')


# 2. N-Queens Problem
print("\n===== N-QUEENS PROBLEM =====")

q = int(input("Enter no. of queens: "))

# Initialize the board with 0s
board = [[0] * q for _ in range(q)]


def is_attack(i, j):
    # Check column
    for k in range(q):
        if board[k][j] == 1:
            return True

    # Check diagonals
    for k in range(q):
        for l in range(q):
            if abs(k - i) == abs(l - j) and board[k][l] == 1:
                return True

    return False


def N_queens(n):
    # If all queens are placed
    if n == 0:
        return True

    for i in range(q):
        for j in range(q):
            if not is_attack(i, j) and board[i][j] != 1:
                board[i][j] = 1

                if N_queens(n - 1):
                    return True

                # Backtrack
                board[i][j] = 0

    return False


if N_queens(q):
    print("\nSolution found:")
    for row in board:
        print(row)
else:
    print("\nNo solution exists for this number of queens.")
