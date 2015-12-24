import sys
import csv

input_path = sys.argv[1]
output_path = sys.argv[2]
with open(input_path, 'r') as f:
    data = f.read()

lines = data.split('\n')
result = []
for l in reversed(lines[:len(lines)-1]):
    if l == '':
        break
    else:
        if l[0] == ' ':
            result.append(l)

s = ''.join(result);
with open(output_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    identifiers = ['0', '1', '2', '3', '4', '5', '.']
    for i in identifiers:
        writer.writerow([i, s.count(i)])
