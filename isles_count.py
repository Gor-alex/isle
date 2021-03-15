from typing import List


def paint_out(x, y, matrix) -> None:
    """
    Paint finded isle (Research for others nodes)
    :param x: x coordinate
    :param y: y coordinate
    :param matrix: research matrix with isles
    :return: None (do something on object)
    """
    # Guarding out of range
    if x >= 0 and x <= len(matrix) - 1 and y >= 0 and y <= len(matrix[x]) - 1:
        # Stop iteration if we have other isle or water
        if matrix[x][y] == 0 or matrix[x][y] == 2:
            return
        # We find isle
        if matrix[x][y] == 1:
            matrix[x][y] = 2

        # Checking nearest nodes
        # [x - 1, y + 1] [x, y + 1] [x + 1, y + 1]
        # [x-1, y]       [*]        [x + 1, y]
        # [x - 1, y -1]  [x,y - 1]  [x + 1, y - 1]
        paint_out(x - 1, y + 1, matrix)
        paint_out(x - 1, y, matrix)
        paint_out(x - 1, y - 1, matrix)
        paint_out(x, y + 1, matrix)
        paint_out(x, y - 1, matrix)
        paint_out(x + 1, y + 1, matrix)
        paint_out(x + 1, y, matrix)
        paint_out(x + 1, y - 1, matrix)


# TODO Расчитать количество островов (Рекурсивно),
# TODO которые размечены в матрице единицами

def isles_count(matrix: List[List[int]]) -> int:
    """
    Count isles in matrix
    :param matrix: input matrix
    :return: int (Count of isles)
    """
    isles = 0
    for i, line in enumerate(matrix):
        for j, node in enumerate(line):
            if node == 1:
                paint_out(i, j, matrix)
                isles += 1

    return isles


test_case_a_3 = [
    [0, 1, 1],
    [0, 1, 1],
    [1, 0, 0],
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0]
]

test_case_a_2 = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0]
]


test_case_a_1 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]


test_case_a_0 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

test_case_a_1_c = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

test_case_a_string = [
    [None, 0, 1],
    [0,    1, 0],
    [0,    0, "a"]
]

test_case_a_minus = [
    [0, 0, -1],
    [0, 1,  0],
    [0, 0,  0]
]

assert isles_count(test_case_a_3) == 3
assert isles_count(test_case_a_2) == 2
assert isles_count(test_case_a_1) == 1
assert isles_count(test_case_a_0) == 0
assert isles_count(test_case_a_string) == 1
assert isles_count(test_case_a_minus) == 1
assert isles_count(test_case_a_1_c) == 1



