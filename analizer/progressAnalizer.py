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

field = ''.join(result);
with open(output_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    identifiers = ['0', '1', '2', '3', '4', '5', '.']
    counts = [field.count(i) for i in identifiers]
    winner = 1 if sum(counts[:3]) < sum(counts[3:6]) else 0
    for i in range(6):
        score = counts[i] + 300 if (i // 3) == winner else counts[i]
        writer.writerow([i, score])
