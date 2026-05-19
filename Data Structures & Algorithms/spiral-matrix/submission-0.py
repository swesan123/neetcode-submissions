class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        direction = "right"
        output = []

        while matrix:
            if direction == "right":
                for n in matrix[0]:
                    output.append(n)

                matrix = matrix[1:]
                direction = "down"

            elif direction == "down":
                for row in matrix:
                    output.append(row[-1])

                matrix = [row[:-1] for row in matrix if row[:-1]]
                direction = "left"

            elif direction == "left":
                for n in reversed(matrix[-1]):
                    output.append(n)

                matrix = matrix[:-1]
                direction = "up"

            elif direction == "up":
                for row in reversed(matrix):
                    output.append(row[0])

                matrix = [row[1:] for row in matrix if row[1:]]
                direction = "right"

        return output