def chesboard_pattern(width, height):
    shesboard = []
    for i in range(height):
        shesboard.append([])
        for j in range(width):
            shesboard[i].append((i + j) % 2)
    return shesboard

if __name__ == "__main__":
  assert chesboard_pattern(2, 2) == [[0, 1], [1, 0]]
  assert chesboard_pattern(4, 3) == [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]


