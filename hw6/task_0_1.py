# перевірка, чи може королева бути розміщена на цій позиції
def can_place(board, row, col):
  for r, c in board:
    if r == row or c == col or abs(r - row) == abs(c - col):
      return False
  return True

def solve(board, row):
  # якщо всі 8 королев розміщені, додати до розв'язку
  if row == 8:
    solutions.append(board[:])
    return
    
  # спробувати розмістити королеву на кожній колонці в поточному рядку
  for col in range(8):
    if can_place(board, row, col):
      board.append((row, col))
      solve(board, row+1)
      board.pop()

solutions = []
solve([], 0)

# вивід знайдених розв'язків
for solution in solutions:
  board = [['.' for _ in range(8)] for _ in range(8)]
  for r, c in solution:
    board[r][c] = 'Q'
  print('\n'.join([''.join(row) for row in board]))
  print()
