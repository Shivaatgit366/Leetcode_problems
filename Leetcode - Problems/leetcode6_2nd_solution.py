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


def zigzag(s, numRows):
    # these are some of the exceptional cases.
    if len(s) == 1:
        return [[s]]
    if len(s) == 2:
        return [[c for c in s]]
    if len(s) > 1 and numRows == 1:
        return [[c for c in s]]
    if len(s) < numRows:
        return [[c for c in s]]

    final_list = []  # this is a list of columns.

    current_column = 0  # current column is 0th column.
    current_row = 0  # current row is 0th row.

    for char in s:
        if current_column % (numRows - 1) == 0:  # this is the first condition.
            # if current_row is zero, then only make an empty list.
            if current_row == 0:
                temp_list = ["" for i in range(numRows)]
            # replaces the item with the character in the string.
            temp_list[current_row] = char
            current_row = current_row + 1  # row increment.
            if current_row == numRows:  # if row becomes numRows, then decrease the row.
                current_row = current_row - 1
                final_list.append(temp_list)
                current_column = current_column + 1
                # make the current row to zero, very important step.
                if current_row == 1:
                    current_row = 0

        else:  # this is the second condition.
            # empty the list every time for this case.
            temp_list = ["" for i in range(numRows)]
            temp_list[current_row - 1] = char
            current_row = current_row - 1
            current_column = current_column + 1
            final_list.append(temp_list)
            # make the current row to zero, very important step.
            if current_row == 1:
                current_row = 0

    if final_list[-1] != temp_list:
        final_list.append(temp_list)
    return final_list


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
