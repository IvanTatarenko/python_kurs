def chesboard_pattern(width, height):
  pattern = "01" * (width // 2) + "0" * (width % 2)
  chessboard = [pattern[i % width:] + pattern[:i % width] for i in range(height)]
  return chessboard

res = chesboard_pattern(8, 8)
print(res)