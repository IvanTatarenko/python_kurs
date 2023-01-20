import json

def split_format(data):
  
  columns = []
  index = []
  data_list = []

  for item in data["data"]:
    for k, v in item.items():
      if k != "index" and k not in columns:
        columns.append(k)

  for item in data["data"]:
    index.append(item["index"])

  for item in data["data"]:
    data_row = []
    for k,v in item.items():
      if k != "index":
        data_row.append(v)
    data_list.append(data_row)

  result = {
    "columns": columns,
    "index": index,
    "data": data_list
  }

  return result

def index_format(data):
  result = {}
  for item in data['data']:
    result[item['index']] = {}
    for col in item.keys():
        if col != 'index':
            result[item['index']][col] = item[col]
  
  return result
  
def column_format(data):
  result = {col: {row["index"]: row[col] for row in data["data"]} for row in data["data"] for col in row if col != "index"}
  
  return result


if __name__ == "__main__":
  with open('hw8/export/split_format.json', 'r', encoding='utf-8') as f: split_format_data = json.load(f)
  with open('hw8/export/index_format.json', 'r', encoding='utf-8') as f: index_format_data = json.load(f)
  with open('hw8/export/column_format.json', 'r', encoding='utf-8') as f: column_format_data = json.load(f)
    
  
  with open('hw8/import/data.json', 'r', encoding='utf-8') as f: 
    data = json.load(f)
    assert split_format(data) == (split_format_data)
    assert index_format(data) == (index_format_data)
    assert column_format(data) == (column_format_data)