import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mflops_all.csv")  # N & time_ms

N = df["N"]

# Compute bandwidth
vector_bw = (N * 4) / (df["vector_time_ms"] / 1000) / 1e9
indirect_bw = (N * 4) / (df["indirect_time_ms"] / 1000) / 1e9

# Percent
peak = 409.6
vector_percent = (vector_bw / peak) * 100
indirect_percent = (indirect_bw / peak) * 100

# Draw
plt.title("Memory Bandwidth Utilization (% of Peak)")
plt.plot(N, vector_percent, "b-o", label="Vector")
plt.plot(N, indirect_percent, "g-^", label="Indirect")
plt.xlabel("Problem Size")
plt.ylabel("% of Peak Bandwidth")
plt.xscale("log")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("bandwidth_percent.png", dpi=300)
plt.show()