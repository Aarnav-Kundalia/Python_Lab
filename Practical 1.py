import pickle
import csv

a = [25, 25.05, 5 + 0j, 25 + 6j]
b = [5, 6.25, 6 + 0j, 5 - 25j]
op = ['+', '-', '*', '/', '//', '%', '**']

results = []

with open("operator_results.txt", "w") as f_txt, \
     open("operator_results.csv", "w", newline='', encoding="utf-8") as f_csv:
    csv_writer = csv.writer(f_csv)
    csv_writer.writerow(["a", "operator", "b", "result", "type/result or error"])
    for o in op:
        f_txt.write(f"\n--- Results for operator '{o}' ---\n")
        for i in range(len(a)):
            for j in range(len(b)):
                try:
                    result = eval(f"{a[i]} {o} {b[j]}")
                    line = f"{a[i]} {o} {b[j]} = {result} (type: {type(result)})"
                    f_txt.write(line + "\n")
                    csv_writer.writerow([a[i], o, b[j], result, type(result)])
                    results.append({"a": a[i], "operator": o, "b": b[j], "result": result, "type": str(type(result))})
                except Exception as e:
                    err_line = f"Error: {e} for operation {a[i]} {o} {b[j]}"
                    f_txt.write(err_line + "\n")
                    csv_writer.writerow([a[i], o, b[j], "Error", str(e)])
                    results.append({"a": a[i], "operator": o, "b": b[j], "result": None, "error": str(e)})

with open("operator_results.pkl", "wb") as f_bin:
    pickle.dump(results, f_bin)