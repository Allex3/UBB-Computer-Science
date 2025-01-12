from copy import deepcopy


def check_rref(matrix: list[list[int]], m: int, n: int) -> bool:

    pos_of_pivot_on_row = [100]*m # 100 if a row has only 0es on it!

    for i in range(m): # check for all elements of the matrix if they are pivots
        for j in range(n):
            # we are parsing the current column, so if we reach a 1
            # mark it as a pivot and go to next row
            if matrix[i][j] == 1:
                pos_of_pivot_on_row[i] = j
                break
        if pos_of_pivot_on_row[i] == 100: #reached the rows of 0es, check if the rows below it are ONLY of 0es
            for zero_row in range(i+1, m):
                for j in range(n):
                    if matrix[zero_row][j] != 0:
                        return False
            break # if reached here all below rows are also 0, so break from the i loop


    # What we care about is that the matrix is in echelon form
    # So if we have a 1 pivot, below it should be only 0es given by the echelon form
    # And logically, the next pivot will be on a higher column than the one before it
    # Otherwise, it wouldn't be in row echelon form
    # Thus, check if the vector of the positions of pivots is strictly ascending
    for i in range(m-1):
        if pos_of_pivot_on_row[i] >= pos_of_pivot_on_row[i+1] and pos_of_pivot_on_row[i]!= 100: #descending and non-zero row
            return False

    # Other than that, we care about the fact that
    # for the pivots, the first ones on a row, to not have another 1 on their column
    # So if they do, return false
    for i in range(m): # go through the pivots of all rows and check their columns
        if pos_of_pivot_on_row[i] != 100: #didn't reach the zero rows yet:
            for j in range(m): # go through all the rows of the current column
                if matrix[j][pos_of_pivot_on_row[i]] != 0 and j != i: #found another 1 in another row on the same column of the pivot
                    return False

    # Now we know that the matrix is in echelon form, from the first and second step
    # And from the third and final step we know that the pivots are the only 1s on their columns
    return True

def print_matrix(matrix: list[list[int]], fd: int) -> None:
    file = open(f"output_1.out", "a")
    for row in matrix:
        for column in row:
            file.write(f"{column} ")
        file.write("\n")
    file.write("\n")

def generate_all_rref(m: int, n: int, matrix: list[list[int]], row_number: int, column_number: int, element: int, fd: int) -> None:
    """
    Function that generates all possible matrices in Z_2 of mxn and checks if they are rref
    :param m: Number of rows
    :param n: Number of columns
    :param matrix: The matrix of mxn
    :param row_number: The row we are currently generating
    :param column_number: The column we are currently generating
    :param element: What to add, 0 or 1
    :return: None
    """

    # Generate all possible matrices mxn with elements only 0 or 1


    if column_number == n: #finished the column (0 to n-1), go to next row
        if row_number == m-1:  # finished generating all rows, so finished last column of last row
            print(matrix)
            if check_rref(matrix, m, n):
                print_matrix(matrix, fd)
            return

        generate_all_rref(m, n, matrix, row_number+1, 0, 0, fd) # add 0
        generate_all_rref(m, n, matrix, row_number + 1, 0, 1, fd)  # add 1
        return

    # We didn't finish a row, nor all the rows, so just go to the next column on the current row, and put the element
    matrix[row_number][column_number] = element
    if column_number+1 == n: # finished the column, so go only down
        generate_all_rref(m, n, matrix, row_number, column_number+1, 0, fd)  # add 0
        return
    generate_all_rref(m, n, matrix, row_number, column_number + 1, 0, fd)
    generate_all_rref(m, n, matrix, row_number, column_number+1, 1, fd)  # add 1 on this position

def count_rref(m: int, n: int) -> int:

def print_count_rref(count: int, m: int, n: int) -> None:
    file = open(f"output_1.out", "w")
    file.write(f"1. the number of matrices A ∈ M({m},{n})(Z2) in reduced echelon form is {count}")



def solve():
    for i in range(1, 6):
        fopen = open(f"input_{i}.in", "r")
        values = fopen.read()
        m = int(values.split(" ")[0])
        n = int(values.split(" ")[1])

        count = count_rref(m, n)
        print_count_rref(count, m, n)

        row = [0]*n
        matrix = []
        for j in range(m):
            matrix.append(deepcopy(row))
        if n<=5 and m<=5:
            generate_all_rref(m, n, matrix, 0, 0, 0, i) #begin with 0 as first element
            generate_all_rref(m, n, matrix, 0, 0, 1, i) # begin with 1 as first element

if __name__=="__main__":
    solve()