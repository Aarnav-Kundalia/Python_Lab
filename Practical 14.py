matrix = []
with open("mu_lifetime.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            matrix.append([int(parts[0]), int(parts[1])])

for row in matrix:
    row[1] = row[1] * 0.1

with open("mu_lifetime(0.1x).txt", "w") as f:
    for row in matrix:
        f.write('\t'.join(str(x) for x in row) + '\n')

def frequency_distribution(data, min, max, num_bins):
    bin_width = (max - min) / num_bins
    bins = [0] * num_bins
    for value in data:
        if min <= value < max:
            index = int((value - min) / bin_width)
            bins[index] += 1
    return bins

data = [row[1] for row in matrix]
min_val = 0
max_val = 20
num_bins = 200
bins = frequency_distribution(data, min_val, max_val, num_bins)


sum_fx = 0  
sum_f = 0   

with open("mu_lifetime_freq_dist.txt", "w") as f:
    bin_centers = []
    for i in range(num_bins):
        bin_start = min_val + i * (max_val - min_val) / num_bins
        bin_end = min_val + (i + 1) * (max_val - min_val) / num_bins
        bin_center = (bin_start + bin_end) / 2
        bin_centers.append(bin_center)
        
      
        sum_fx += bins[i] * bin_center
        sum_f += bins[i]
        
        f.write(f"{bin_start:.6f}\t{bin_end:.6f}\t{bin_center:.6f}\t{bins[i]}\n")


mean = sum_fx / sum_f if sum_f > 0 else 0
print(f"Mean of frequency distribution: {mean:.6f}")
print(f"Total observations: {sum_f}")

def nth_moment(centers, freqs, n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    total_f = sum(freqs)
    if total_f == 0:
        return 0.0
    moment_sum = 0.0
    for c, f in zip(centers, freqs):
        moment_sum += (c ** n) * f
    return moment_sum / total_f

try:
    n_input = input("Enter n for the nth moment (non-negative integer): ")
    n_val = int(n_input)
    if n_val < 0:
        raise ValueError
    moment_value = nth_moment(bin_centers, bins, n_val)
    print(f"{n_val}th moment about origin: {moment_value:.6f}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")