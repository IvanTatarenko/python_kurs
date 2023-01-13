#[[0, 2, 4, 1, 3], [0, 3, 1, 4, 2], [1, 3, 0, 2, 4], [1, 4, 2, 0, 3], [2, 0, 3, 1, 4], [2, 4, 1, 3, 0], [3, 0, 2, 4, 1], [3, 1, 4, 2, 0], [4, 1, 3, 0, 2], [4, 2, 0, 3, 1]]


result = [[0, 2, 4, 1, 3], [0, 3, 1, 4, 2]]
def main(result):
  rows = 5
  columns = 5 
  new_res =  [1, 3, 0, 2, 4]
  if no_repetition(result, new_res):
    result.append(new_res)
 

def no_repetition(result, new_res):
  for res in result:
    if res == new_res: return False
  return True

def add_queen(new_res):
  pass

# def queen_main(rows, cols):
#   if rows <= 0:
#     return [[]] 
#   else:
#     return add_queen(rows - 1, cols, queen_main(rows - 1, cols))

# def add_queen(new_row, cols, known_solutions):
#   new_solutions = []
#   for solution in known_solutions:
#     for new_column in range(cols):
#       if no_conflict(new_row, new_column, solution):
#         new_solutions.append(solution + [new_column])
#   return new_solutions

# def no_conflict(new_row, new_column, solution):
#   for row in range(new_row):
#     if solution[row] == new_column  or solution[row] + row == new_column + new_row or solution[row] - row == new_column - new_row:
#       return False
#   return True



print(main(result))

print(result)
# boards = queenproblem(8, 8)
# for i in  range(len(boards)):
#   board = []
#   print