def can_knight_capture_pawn(knight_pos, pawn_pos):
  """
  Функція, яка перевіряє, чи може кінь побити пішака за 2 ходи.

  :param knight_pos: координати кіння у шахматній нотації, наприклад 'a1'
  :param pawn_pos: координати пішака у шахматній нотації, наприклад 'b2'
  :return: True, якщо кінь може побити пішака за 2 ходи, і False, якщо ні.
  """
  # Перевірка, чи може кінь переміститись на клітинку пішака з одного ходу
  dx = abs(ord(knight_pos[0]) - ord(pawn_pos[0]))
  dy = abs(int(knight_pos[1]) - int(pawn_pos[1]))
  if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    return True
    
  # Шукаємо можливі клітинки, на які може переміститись кінь
  possible_moves = []
  for dx, dy in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
    new_x = ord(knight_pos[0]) + dx
    new_y = int(knight_pos[1]) + dy
    if 'a' <= chr(new_x) <= 'h' and 1 <= new_y <= 8:
      possible_moves.append(chr(new_x) + str(new_y))
    
  # Перевіряємо, чи може кінь дістатись до клітинки пішака за 2 ходи
  for move in possible_moves:
    if len(move) != 2:  # перевірка дійсності значення move
      continue
    dx = abs(ord(move[0]) - ord(pawn_pos[0]))
    dy = abs(int(move[1]) - int(pawn_pos[1]))
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
      # Виводимо дошку та шлях коня
      print_board(knight_pos, pawn_pos, move)
      return True
    
  return False


def print_board(knight_pos, pawn_pos, knight_path):
  """
  Функція, яка відображає дошку та шлях коня.

  :param knight_pos: координати кіння у шахматній нотації
  :param pawn_pos: координати пішака у шахматній нотації
  :param knight_path: список координат клітинок, на які переміщувався кінь
  """
  board = [['.' for _ in range(8)] for _ in range(8)]
  x, y = ord(pawn_pos[0]) - 97, int(pawn_pos[1]) - 1
  board[y][x] = 'P'
  x, y = ord(knight_pos[0]) - 97, int(knight_pos[1]) - 1
  board[y][x] = 'K'
  for move in knight_path:
    if len(move) != 2 or not move[0].isalpha() or not move[1].isdigit():
      continue
    x, y = ord(move[0]) - 97, int(move[1]) - 1
    board[y][x] = 'x'
  for row in board:
    print(' '.join(row))

# Приклад використання
print(can_knight_capture_pawn('c3', 'd6')) # Повинно вивести True та дошку з шляхом коня

