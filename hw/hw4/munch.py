import hw4_206867517 as hw
import time


def winnable(board):
    """ determines if in a given configuration, represented by board,
        the player who makes the current move can force a win.
        board[i] is the height of column i
        show: if True and the configuration can force win,
        a possible move printed.
    """
    if sum(board) == 0:  # halting after the (losing) move (0,0)
        return True

    m = len(board)

    for i in range(m):  # for every column i
        for j in range(board[i]):  # for every possible cell (i,j)
            # generate new munched board
            munched_board = board[0:i] + [min(board[k], j) for k in range(i, m)]

            # recursion
            if not winnable(munched_board):  # if munched board is losing
                return True

    return False  # current board cannot force win


lst = [16]
for i in lst:
    t0 = time.perf_counter()
    hw.winnable_mem([5]*i)
    t1 = time.perf_counter()
    print("with memoization: ", hw.count)

    # t0 = time.perf_counter()
    # winnable([5] * i)
    # t1 = time.perf_counter()
    # print("no memoization: ", t1 - t0)

