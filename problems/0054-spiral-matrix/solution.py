class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sol =[]
        while matrix:
            sol += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    sol.append(row.pop())
            if matrix:
                sol += (matrix.pop()[::-1])
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    sol.append(row.pop(0))


        return sol

        