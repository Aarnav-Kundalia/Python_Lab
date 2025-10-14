matrix = []
with open("multi_coloumn_1000.txt", "r") as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) == 4:
            matrix.append([float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])])

matrix.sort(key=lambda x: x[2])

with open("multi_coloumn_1000(sorted).txt", "w") as f:
    for row in matrix:
        f.write('\t'.join(str(x) for x in row) + '\n')