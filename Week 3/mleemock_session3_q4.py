# mleemock@uwo.ca
# date: june 24th, 2024

class numMatrix:
    def __init__(self, matrix):

        # Check if the matrix is empty or the first row is empty
        if not matrix or not matrix[0]:
            return
        
        # Initialize the number of rows and columns
        self.rows, self.cols = len(matrix), len(matrix[0])

        # Create the prefixSum matrix with an extra row and column filled with zeros
        self.prefixSum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
         # Fill the prefixSum matrix with cumulative sums
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self.prefixSum[i][j] = (
                    matrix[i-1][j-1] 
                    + self.prefixSum[i-1][j] 
                    + self.prefixSum[i][j-1] 
                    - self.prefixSum[i-1][j-1]
                )
    
    # Calculate the sum of the region defined by (row1, col1) to (row2, col2)
    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.prefixSum[row2+1][col2+1]
            - self.prefixSum[row1][col2+1]
            - self.prefixSum[row2+1][col1]
            + self.prefixSum[row1][col1]
        )

# Example usage
matrix1 = numMatrix([
    [3, 0, 1, 4, 2], 
    [5, 6, 3, 2, 1], 
    [1, 2, 0, 1, 5], 
    [4, 1, 0, 1, 7], 
    [1, 0, 3, 0, 5]
])

print(matrix1.sumRegion(2, 1, 4, 3)) # Output: 8
print(matrix1.sumRegion(1, 1, 2, 2)) # Output: 11
print(matrix1.sumRegion(1, 2, 2, 4)) # Output: 12

matrix2 = numMatrix([
    [3, 1, 1, 4, 2], 
    [2, 6, 4, 2, 1], 
    [1, 2, 0, 1, 7], 
    [4, 1, 7, 1, 7], 
    [1, 9, 1, 1, 1]
])

print(matrix1.sumRegion(2, 1, 2, 3)) # Output: 3
print(matrix1.sumRegion(1, 1, 2, 2)) # Output: 11
print(matrix1.sumRegion(1, 2, 1, 4)) # Output: 6