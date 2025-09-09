import os
import re
import pandas as pd

# Logs path
log_folder = "logs_cp1"
methods = ["direct", "vector", "indirect"]
results = {m: {} for m in methods}

n_pattern = re.compile(r"problem size N=(\d+)")
time_pattern = re.compile(r"Elapsed time: (\d+\.?\d*) ms")

for method in methods:
    path = os.path.join(log_folder, f"bench_{method}.log")
    with open(path, "r") as f:
        lines = f.readlines()

    current_n = None
    for line in lines:
        n_match = n_pattern.search(line)
        t_match = time_pattern.search(line)

        if n_match:
            current_n = int(n_match.group(1))
            if current_n not in results[method]:
                results[method][current_n] = []
        if t_match and current_n:
            results[method][current_n].append(float(t_match.group(1)))

problem_sizes = sorted(set.union(*(set(results[m].keys()) for m in methods)))
df = pd.DataFrame({"N": problem_sizes})

for method in methods:
    avg_times = [sum(results[method].get(n, [])) / len(results[method].get(n, [1])) for n in problem_sizes]
    df[f"{method}_time_ms"] = avg_times
    df[f"{method}_MFLOPs"] = [round(n / (t / 1000.0) / 1e6, 2) for n, t in zip(problem_sizes, avg_times)]


# Convert time to seconds
df["vector_time_s"] = df["vector_time_ms"] / 1000
df["indirect_time_s"] = df["indirect_time_ms"] / 1000

# float = 4B
df["vector_GBps"] = (df["N"] * 4) / df["vector_time_s"] / 1e9
df["indirect_GBps"] = (df["N"] * 4) / df["indirect_time_s"] / 1e9

# Perlmutter CPU
peak_bw = 409.6  # GB/s
df["vector_%peak_bw"] = df["vector_GBps"] / peak_bw * 100
df["indirect_%peak_bw"] = df["indirect_GBps"] / peak_bw * 100

# Latency unit:ns
df["vector_latency_ns"] = df["vector_time_s"] / df["N"] * 1e9
df["indirect_latency_ns"] = df["indirect_time_s"] / df["N"] * 1e9

# Result
print("\nPerformance Summary Table:\n")
print(df)

df.to_csv("mflops_all.csv", index=False)

df[["N", "vector_%peak_bw", "indirect_%peak_bw"]].to_csv("bandwidth_percent.csv", index=False)
df[["N", "vector_latency_ns", "indirect_latency_ns"]].to_csv("latency_ns.csv", index=False)
