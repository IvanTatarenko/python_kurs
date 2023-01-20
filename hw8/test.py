import unittest
from task_1 import *
from task_2 import *
from task_3 import *
from task_4 import *
from task_5 import *
from task_7 import *
class TestTask_1(unittest.TestCase):
    
  def test_chesboard_pattern(self):
    # task 1
    self.assertEqual(chesboard_pattern(2,2), [[0, 1], [1, 0]])
    self.assertEqual(chesboard_pattern(4, 3), [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]])
    # task 2
    self.assertEqual(bigger_then_half([1, 2, 3]), 3)
    self.assertEqual(bigger_then_half([1, 2, 2, 3]), 3)
    self.assertEqual(bigger_then_half([1, 1, 1, 2, 3]), 2)
    self.assertEqual(bigger_then_half([1, 1, 2, 2, 3]), 3)
    # task 3
    self.assertEqual(sum_list([1, 2, "1"]), 4)
    self.assertEqual(type(sum_list([1, 2, "1"])), int)
    self.assertEqual(sum_list([1, 2, "1", "1.1"]), 5.1)
    self.assertEqual(type(sum_list([1, 2, "1", "1.1"])), float)
    self.assertEqual(sum_list([1, 2, "1", "-1.0"]), 3)
    self.assertEqual(type(sum_list([1, 2, "1", "-1.0"])), int)
    #task 4
    self.assertEqual(divide((1, 8), (3, 8)), (1, 2))
    self.assertEqual(divide((1, 0), (3, 8)), None)
    #task 5
    self.assertEqual(palindrom('asdsa'), True)
    self.assertEqual(palindrom('asddsa'), True)
    self.assertEqual(palindrom('івааві'), True)
    self.assertEqual(palindrom('івааasdfasdfві'), False)
    # task 7
    with open('data.json', 'r', encoding='utf-8') as f:
      text = json.load(f)
      self.assertEqual(column_format(text), {
        "col 1": {
          "row 1": "a",
          "row 2": "c"
        },
        "col 2": {
          "row 1": "b",
          "row 2": "d"
        }
      })


    
if __name__ == "__main__":
  unittest.main()