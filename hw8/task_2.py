def bigger_then_half(array):
  return max(sum(array) // len(array), array[len(array) // 2] + 1)

if __name__ == "__main__":
  assert bigger_then_half([1, 2, 3]) == 3
  assert bigger_then_half([1, 2, 2, 3]) == 3
  assert bigger_then_half([1, 1, 1, 2, 3]) == 2
