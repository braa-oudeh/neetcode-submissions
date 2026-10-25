class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_remove = []
        cols_to_remove = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows_to_remove.append(i)
                    cols_to_remove.append(j)

        for r in range(len(rows_to_remove)):
            for c in range(len(matrix[0])):          # fixed: columns, not rows
                matrix[rows_to_remove[r]][c] = 0

        for c in range(len(cols_to_remove)):
            for r in range(len(matrix)):
                matrix[r][cols_to_remove[c]] = 0

        