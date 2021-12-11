# Skeleton file for HW4 - Winter 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_ID.py).


def winnable_mem(board):
    d = {}
    return winnable_mem_rec(board, d)


# 1c
def winnable_mem_rec(board, d):
    """  recursive solution with memoization to munch! game."""
    if sum(board) == 0:  # halting after the (losing) move (0,0)
        return True
    board_imu = tuple(board)
    if board_imu in d:
        return d[board_imu]
    m = len(board)

    for i in range(m):  # for every column i
        for j in range(board[i]):  # for every possible cell (i,j)
            # generate new munched board
            munched_board = board[0:i] + [min(board[k], j) for k in range(i, m)]
            munched_board_imu = tuple(munched_board)
            # recursion
            if not winnable_mem_rec(munched_board, d):  # if munched board is losing
                d[munched_board_imu] = False
                return True
            else:
                d[munched_board_imu] = True
    return False  # current board cannot force win


# 2a

def H_local(n, i, j):
    block_size = pow(2, n - 1)  # O(n)
    return H_local_rec(n, i, j, block_size)


def H_local_rec(n, i, j, block_size):
    if n == 0:  # O(logn)
        return 0
    if i >= block_size and j >= block_size:
        return 1 - H_local_rec(n - 1, i % block_size, j % block_size, block_size // 2)  # 5*O(logn)
    else:
        return H_local_rec(n - 1, i % block_size, j % block_size, block_size // 2)  # 4*O(logn)


# 2c
H_complete = lambda n: [[H_local(n, i, j) for j in range(pow(2, n))] for i in range(pow(2, n))]


# 3a
def can_create_once(s, L):
    return can_create_once_rec(s, L, 0)


def can_create_once_rec(s, L, left):
    if left > len(L) - 1 and s == 0:  # O(1)
        return True
    elif left > len(L) - 1 and s != 0:  # O(1)
        return False
    return can_create_once_rec(s - L[left], L, left + 1) or can_create_once_rec(s + L[left], L, left + 1)  # O(1)


# 3b
def can_create_twice(s, L):
    return can_create_twice_rec(s, L, 0)


def can_create_twice_rec(s, L, left):
    if left > len(L) - 1 and s == 0:  # O(1)
        return True
    elif left > len(L) - 1 and s != 0:  # O(1)
        return False
    return can_create_twice_rec(s, L, left + 1) or can_create_twice_rec(s + L[left], L, left + 1) \
           or can_create_twice_rec(s + 2 * L[left], L, left + 1) or can_create_twice_rec(s - L[left], L, left + 1) \
           or can_create_twice_rec(s - 2 * L[left], L, left + 1)  # O(1)


# 3c
def valid_braces_placement(s, L):
    if len(L) == 3:  # O(1)
        return eval("".join(str(i) for i in L)) == s  # O(n)
    for op in range(1, len(L), 2):  # O(n**2)
        if valid_braces_placement(s,
                                  L[:op - 1] + [eval("".join(str(i) for i in L[op - 1:op + 2]))] + L[op + 2:]):  # O(n)
            return True

    return False


# 4a
def grid_escape1(B):
    return grid_escape1_rec(B, 0, 0, len(B))


def grid_escape1_rec(B, i, j, n):
    if n == 0:
        return True
    if i == n - 1 and j == n - 1:
        return True
    if i > n - 1 or j > n - 1:
        return False
    if B[i][j] == 0:
        return False
    return grid_escape1_rec(B, i + B[i][j], j, n) or grid_escape1_rec(B, i, j + B[i][j], n)


# 4b
def grid_escape2(B):
    n = len(B)
    visited = [[False for j in range(n)] for i in range(n)]  # "memoize" visited cells
    return grid_escape2_rec(B, 0, 0, n, visited)


def grid_escape2_rec(B, i, j, n, visited):
    if n == 0:
        return True
    if i == n - 1 and j == n - 1:
        return True
    if not ((n > i >= 0) and (n > j >= 0)):
        return False
    up = i + B[i][j]
    down = i - B[i][j]
    left = j - B[i][j]
    right = j + B[i][j]
    if up < n and not visited[up][j]:
        visited[i][j] = True
        if grid_escape2_rec(B, up, j, n, visited):
            return True
        else:
            visited[i][j] = False
    if down >= 0 and not visited[down][j]:
        visited[i][j] = True
        if grid_escape2_rec(B, down, j, n, visited):
            return True
        else:
            visited[i][j] = False
    if left >= 0 and not visited[i][left]:
        visited[i][j] = True
        if grid_escape2_rec(B, i, left, n, visited):
            return True
        else:
            visited[i][j] = False
    if right < n and not visited[i][right]:
        visited[i][j] = True
        if grid_escape2_rec(B, i, right, n, visited):
            return True
        else:
            visited[i][j] = False
    return False


##########
# Tester #
##########
def test():
    # 1c
    if winnable_mem([5, 5, 3]) or \
            not winnable_mem([5, 5, 5]) or \
            winnable_mem([1]) or not winnable_mem([]) or not winnable_mem([2]) or winnable_mem([2, 1]):
        print("error in winnable_mem")
    # 2a
    if H_local(2, 2, 2) != 1:
        print("error in H_local")
    # 2c
    if H_complete(1) != [[0, 0], [0, 1]]:
        print("error in H_complete")
    # 3a
    if not can_create_once(6, [5, 2, 3]) or not can_create_once(-10, [5, 2, 3]) \
            or can_create_once(9, [5, 2, 3]) or can_create_once(7, [5, 2, 3]):
        print("error in can_create_once")
    # 3b
    if not can_create_twice(6, [5, 2, 3]) or not can_create_twice(9, [5, 2, 3]) \
            or not can_create_twice(7, [5, 2, 3]) or can_create_twice(19, [5, 2, 3]) or can_create_twice(2, []):
        print("error in can_create_twice")
    # 3c
    L = [6, '-', 4, '*', 2, '+', 3]
    if not valid_braces_placement(10, L) or not valid_braces_placement(1, L) or valid_braces_placement(5, L):
        print("error in valid_braces_placement")

    B1 = [[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]
    B2 = [[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]
    B3 = [[2, 1, 2, 1], [1, 2, 1, 1], [2, 2, 2, 2], [4, 4, 4, 4]]

    # 4a
    if grid_escape1(B1) is False:
        print("error in grid_escape1 - B1")
    if grid_escape1(B2) is True:
        print("error in grid_escape1 - B2")
    if grid_escape1(B3) is True:
        print("error in grid_escape1 - B3")

    # 4b
    if grid_escape2(B1) is False:
        print("error in grid_escape2 - B1")
    if grid_escape2(B2) is False:
        print("error in grid_escape2 - B2")
    if grid_escape2(B3) is True:
        print("error in grid_escape2 - B3")
