import pandas as pd
import matplotlib.pyplot as plt

# ---- Load the CSV files ----
file1 = r"C:\Users\iansp\OneDrive\Desktop\Pressure Sensor data\Station 1 Third 8-21.csv"
file2 = r"C:\Users\iansp\OneDrive\Desktop\Pressure Sensor data\Station 1 Third 8-22.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# ---- Clean column names (in case of extra spaces) ----
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

directions = ["North", "East", "South", "West"]
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

# ---- Normalize each direction so its average becomes 0 ----
df1_norm = df1.copy()
df2_norm = df2.copy()

for direction in directions:
    df1_norm[direction] = df1[direction] - df1[direction].mean()
    df2_norm[direction] = df2[direction] - df2[direction].mean()

# ---- Create side-by-side subplots ----
fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

# --- Plot file 1 (normalized) ---
for direction, color in zip(directions, colors):
    axes[0].plot(df1_norm["Elapsed Seconds"], df1_norm[direction], label=direction, color=color)
axes[0].set_title(f"{file1.split(chr(92))[-1]} (Normalized)")
axes[0].set_xlabel("Elapsed Seconds")
axes[0].set_ylabel("Deviation from Original Average")
axes[0].axhline(0, color="black", linewidth=1)
axes[0].legend()
axes[0].grid(True)

# --- Plot file 2 (normalized) ---
for direction, color in zip(directions, colors):
    axes[1].plot(df2_norm["Elapsed Seconds"], df2_norm[direction], label=direction, color=color)
axes[1].set_title(f"{file2.split(chr(92))[-1]} (Normalized)")
axes[1].set_xlabel("Elapsed Seconds")
axes[1].axhline(0, color="black", linewidth=1)
axes[1].legend()
axes[1].grid(True)

plt.suptitle("Normalized Sensor Readings Comparison: 8-21 vs 8-22", fontsize=14)
plt.tight_layout()
plt.show()

for direction in directions:
    print(direction + "\n")
    print(df1_norm[direction].mean())
    print(df2_norm[direction].mean())
    print(df1_norm[direction].std())
    print(df2_norm[direction].std())
    print("\n")
