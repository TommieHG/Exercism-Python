class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

        #Using list comprehension and transposing to extract rows and columns
        self.rows = [[int(n) for n in row.split()] for row in self.matrix_string.split("\n")]
        self.columns = [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]
        
    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
            
