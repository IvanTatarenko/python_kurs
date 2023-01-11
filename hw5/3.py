def list_to_string(array):
    string = ""
    for i in array:
      string += str(i)
    return(string)

assert list_to_string(["l", "i", "s", "t"]) == "list"
assert list_to_string(["l", "i", "s", "t", 5, 1.1]) == "list51.1"