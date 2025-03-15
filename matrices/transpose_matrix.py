# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's 
# row and column indices.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:

# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

from typing import List

matrix_2x3 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_3x3 = [
    [1, 2, 3],
    [4, 5, 6]
    [1, 2, 42]
]

class SolutionFast:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip(*matrix)]
      
class SolutionLogic:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrixR = [[] for _ in range(len(matrix[0]))] 

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrixR[j].append(matrix[i][j])
                
        return matrixR

solution_fast = SolutionFast()
transposed_matrix_fast = solution_fast.transpose(matrix_2x3) 
print("Transposta usando SolutionFast:", transposed_matrix_fast)

# Usar a classe SolutionLogic
solution_logic = SolutionLogic()
transposed_matrix_logic = solution_logic.transpose(matrix_3x3)  
print("Transposta usando SolutionLogic:", transposed_matrix_logic)

        