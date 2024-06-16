
def diagonal_traversal(A, down=False):
    # traverse matrix up-right diagonally

    nrow = len(A)
    ncols = len(A[0])

    # there are nrow + ncols - 1 diagonals
    for line in range(1, nrow + ncols):
        # find the column we're starting on
        start_col = max(line - nrow, 0)

        # find the number of elements in the diagonal
        count = min(line, nrow, ncols - start_col)

        # print the diagonal
        for j in range(0, count):
            if down:
                if line < nrow:
                    start_row = nrow - count
                else:
                    start_row = 0
                print(A[start_row + j][start_col + j], end=" ")
            else:
                start_row = min(line, nrow) - 1
                print(A[start_row - j][start_col + j], end=' ')


def down_left_diagonal_traversal(A):
    # code here 
    ans = []
    nrow = len(A)
    ncol = len(A[0])
    for line in range(1, nrow + ncol):
        # find starting column
        start_row = max(0, line-ncol)
        
        # find number of elements in diagonal
        count = min(line, ncol, nrow - start_row)
        
        # traverse
        for j in range(count):
            start_col = min(line-1, ncol-1)
            ans.append(A[start_row + j][start_col - j])
    
    return ans


if __name__ == '__main__':
    A = [[1, 2, 3, 4],
         [5, 1, 2, 3],
         [6, 5, 1, 2]]
    
    # print("up right diagonal traversal")
    # diagonal_traversal(A)
    # print()

    # print("down right diagonal traversal")
    # diagonal_traversal(A, down=True)
    # print()

    print(down_left_diagonal_traversal(A))
