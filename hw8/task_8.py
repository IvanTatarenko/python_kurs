import csv
import json

def boxes_capacity():
  with open('hw8/import/boxes.csv', 'r', encoding='utf-8') as f: 
    reader = csv.reader(f)
    data = []
    for row in reader:
      if(row != ['heigh\tlenth\twidth']):
        heigh = int(row[0].split('\t')[0])
        lenth = int(row[0].split('\t')[1])
        width = int(row[0].split('\t')[2])
        data.append([heigh, lenth, width, (heigh*lenth*width)])
    return data    

def export_csv(data):
  f = open('hw8/export/boxes_capacity.csv', 'w')
  f.write('heigh\tlenth\twidth\tcapacity'+ '\n')
  for i in data:
    f.write(str(i[0]) + '\t' + str(i[1]) + '\t' + str(i[2]) + '\t' + str(i[3]) + '\n')
    
def count_json():
  with open('hw8/export/boxes_capacity.csv', 'r', encoding='utf-8') as f: 
    reader = csv.reader(f)
    result_heigh = 0.0
    result_lenth = 0.0
    result_width = 0.0
    result_capacity = 0.0
    counts = 0
    for row in reader:
      if(row != ['heigh\tlenth\twidth\tcapacity']):
        result_heigh += int(row[0].split('\t')[0])
        result_lenth += int(row[0].split('\t')[1])
        result_width += int(row[0].split('\t')[2])
        result_capacity += int(row[0].split('\t')[3])
        counts += 1
    
    result_heigh = result_heigh / counts
    result_lenth = result_lenth / counts
    result_width = result_width / counts
    result_capacity = result_capacity / counts
    result = {
      'average_height': ("%.2f" % result_heigh),
      'average_lenth': ("%.2f" % result_lenth),
      'average_widht': ("%.2f" % result_width),
      'average_capacity': ("%.2f" % result_capacity)
    }
    return result

if __name__ == "__main__":
  capacity = boxes_capacity()
  export_csv(capacity)
  json_res = count_json()
  with open('hw8/export/average_boxes.json', 'w') as f:
    f.write(json.dumps(json_res))