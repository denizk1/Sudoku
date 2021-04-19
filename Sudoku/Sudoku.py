class sudoku:
    def __init__(self, sudokuboxlist):
        self.boxlist = sudokuboxlist  # sudoku box list

    def train(self):  # We will try all sudoku boxes in the list
        for i, X in enumerate(self.boxlist):
            if self.isSudokuBox(X):
                print("Box", i + 1, "is legal")
            else:
                print("Box", i + 1, "is not legal")

    def isSudokuBox(self, sudokubox):
        self.sudlist = [*range(1, 10)]  # Since the sudoku box will be from 1 to 9, we have created a list.
        self.box = sudokubox
        for i in self.box:
            for j in i:
                if (
                        j > 9) and j < 1 and 0 < j < 1:  # If our number is greater than 9, a number less than 1 and is between 0 and 1, it returns false because there is no sudoku box.
                    return False
                if j in self.sudlist:  # If our number is in the sudoku list, it will remove it from the list. Because we won't use it again
                    self.sudlist.remove(j)
        # Since all numbers in the Sudoku box must be found 1 time, and if they are not found, there is a residue in the sudoku list
        # in this case it will turn wrong
        if len(self.sudlist) != 0:
            return False
        return True  # If there are no elements left in the list, all numbers are used 1 times. Returns True


A1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
A2 = [[8, 6, 2],
      [7, 9, 4],
      [3, 1, 5]]
A3 = [[9, 8, 2],
      [1, 3, 5],
      [6, 2, 1]]
A4 = [[5, 1, 0],
      [9, 4, 7],
      [3, 0, 2]]
A5 = [[5, -3, 4],
      [9, 4, 7],
      [3, 1, 12]]
A = [A1, A2, A3, A4, A5]
sudoku = sudoku(A)
sudoku.train()