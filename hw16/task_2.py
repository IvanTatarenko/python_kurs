def inc_str(text):
  if not text or not text[-1].isdigit():
    return text + "1"
  else:
    suffix_len = 1
    while suffix_len <= len(text) and text[-suffix_len].isdigit():
      suffix_len += 1
    suffix = text[-suffix_len+1:]
    new_suffix = str(int(suffix) + 1).zfill(len(suffix))
    return text[:-suffix_len+1] + new_suffix

assert inc_str("foobar") == "foobar1"
assert inc_str("foobar0") == "foobar1"
assert inc_str("foobar00") == "foobar01"
assert inc_str("foobar00001") == "foobar00002"
assert inc_str("foobar0010") == "foobar0011"
assert inc_str("foobar00101") == "foobar00102"