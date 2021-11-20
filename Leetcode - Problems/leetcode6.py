s = "ABCD"
numRows = 2


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        m = zigzag(s, numRows)
        n = transpose_matrix(m)

        output = ""
        for i in n:
            text = "".join(i)
            output = output + text
        return output


def zigzag(stringg, row_count):
    if len(stringg) == 1:
        return [[stringg]]
    if len(stringg) == 2:
        return [[c for c in stringg]]
    if len(stringg) > 1 and row_count == 1:
        return [[c for c in stringg]]
    if len(stringg) < row_count:
        return [[c for c in stringg]]

    matrix = []  # this is a list of columns.

    current_column = 0  # current column is 0th column.
    current_row = 0
    column_values = ["" for x in range(row_count)]  # ["P", "A", "Y", "P"]

    for character in stringg:
        column_count_mod = current_column % (row_count - 1)
        if column_count_mod == 0:
            if current_row == 0:
                column_values = ["" for x in range(row_count)]
            column_values[current_row] = character
            if current_row == (row_count - 1):
                current_row = current_row - 1
                matrix.append(column_values)
                current_column = current_column + 1
            else:
                current_row = current_row + 1
        else:
            column_values = ["" for x in range(row_count)]
            column_values[current_row] = character
            matrix.append(column_values)
            current_row = current_row - 1
            current_column = current_column + 1
    if matrix[-1] != column_values:
        matrix.append(column_values)
    return matrix


def matrix_rows_count(matrix):
    val = 0
    for x in matrix:
        val = val + 1
    return val


def matrix_column_count(matrix):
    val = 0
    for x in matrix[0]:
        val = val + 1
    return val


def matrix_creator(m, n):  # m x n matrix with every value = 1.
    output_list = []
    for x in range(m):
        list1 = []
        for y in range(n):
            value = 1
            list1.append(value)
        output_list.append(list1)
    return output_list


def transpose_matrix(matrics):
    num_rows = matrix_rows_count(matrics)
    num_column = matrix_column_count(matrics)
    virtual_matrix = matrix_creator(num_column, num_rows)

    for i in range(len(matrics)):
        for j in range(len(matrics[i])):
            virtual_matrix[j][i] = matrics[i][j]
    return virtual_matrix


gg = Solution()
print(gg.convert(s, numRows))
