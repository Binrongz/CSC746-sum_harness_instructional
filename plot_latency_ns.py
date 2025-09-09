import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mflops_all.csv")
N = df["N"]

# Compute latency unit:ns
vector_latency = (df["vector_time_ms"] / 1000) / N * 1e9
indirect_latency = (df["indirect_time_ms"] / 1000) / N * 1e9

# Draw
plt.title("Memory Access Latency (ns/access)")
plt.plot(N, vector_latency, "b-o", label="Vector")
plt.plot(N, indirect_latency, "g-^", label="Indirect")
plt.xlabel("Problem Size")
plt.ylabel("Latency (ns/access)")
plt.xscale("log")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("latency_ns.png", dpi=300)
plt.show()
