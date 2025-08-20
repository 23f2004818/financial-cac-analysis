"""
Financial Services Performance Analysis - CAC 2024
Author email for verification: 23f2004818@ds.study.iitm.ac.in

Outputs:
- plots/cac_trend.png            (CAC by quarter + industry target)
- plots/gap_to_target.png        (Gap vs. target per quarter)
- Console prints with summary stats (avg CAC, % over target, gap)
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Config & constants
# ----------------------------
INDUSTRY_TARGET = 150.0
EMAIL = "23f2004818@ds.study.iitm.ac.in"

# ----------------------------
# Load data
# ----------------------------
data_path = os.path.join("data", "cac_2024.csv")
df = pd.read_csv(data_path)

# Ensure correct order
order = ["Q1", "Q2", "Q3", "Q4"]
df["quarter"] = pd.Categorical(df["quarter"], categories=order, ordered=True)
df = df.sort_values("quarter").reset_index(drop=True)

# ----------------------------
# Calculations
# ----------------------------
df["gap_to_target"] = df["cac"] - INDUSTRY_TARGET
avg_cac = df["cac"].mean()
gap_avg = avg_cac - INDUSTRY_TARGET
pct_over_target = (gap_avg / INDUSTRY_TARGET) * 100

# Print key results for quick review
print(f"Verification email: {EMAIL}")
print("Quarterly CAC:")
print(df[["quarter", "cac"]].to_string(index=False))
print(f"\nAverage CAC (should be 230.13): {avg_cac:.2f}")
print(f"Industry target: {INDUSTRY_TARGET:.2f}")
print(f"Average gap vs. target: {gap_avg:.2f}")
print(f"% over target: {pct_over_target:.1f}%")

# ----------------------------
# Visualizations
# ----------------------------
os.makedirs("plots", exist_ok=True)
sns.set_theme(style="whitegrid", context="talk")

# 1) CAC trend vs target line
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="quarter", y="cac", marker="o", linewidth=3)
plt.axhline(INDUSTRY_TARGET, linestyle="--", linewidth=2, color="red", label=f"Industry Target ({INDUSTRY_TARGET:.0f})")
plt.title("Customer Acquisition Cost (CAC) – 2024 Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("CAC")
plt.legend()
plt.tight_layout()
plt.savefig("plots/cac_trend.png", dpi=200)
plt.close()

# 2) Gap to target per quarter (bar)
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="quarter", y="gap_to_target", edgecolor="black")
plt.axhline(0, color="red", linestyle="--", linewidth=2)
plt.title("Gap to Industry Target by Quarter (CAC - 150)")
plt.xlabel("Quarter")
plt.ylabel("Gap vs Target")
plt.tight_layout()
plt.savefig("plots/gap_to_target.png", dpi=200)
plt.close()

# Simple assertion to help keep the README consistent
assert round(avg_cac, 2) == 230.13, "Average CAC must be 230.13 for this dataset."
