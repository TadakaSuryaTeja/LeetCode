from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat

        result_list = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                result_list.append(mat[row][col])
        matrix_result = []
        n = 0
        for row in range(r):
            temp_matrix = []
            for col in range(c):
                temp_matrix.append(result_list[n])
                n += 1
            matrix_result.append(temp_matrix)

        return matrix_result

    def matrixReshape_2(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat

        for i in mat[1:]:
            mat[0] += i
        mat = mat[0]

        newmat = []
        for i in range(r):
            newmat.append(mat[:c])
            mat = mat[c:]

        return newmat
