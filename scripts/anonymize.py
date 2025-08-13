# ==========================================
# Data Anonymization for Financial Data
# Author: Harini J
# ==========================================

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
file_path = "data/creditTest_sample.csv"
data = pd.read_csv(file_path)
anonymized_data = data.copy()

# -----------------------------
# Data Cleaning & Preprocessing
# -----------------------------
# 1. Remove duplicates
data.drop_duplicates(inplace=True)
anonymized_data = data.copy()

# 2. Handle missing values
for col in data.columns:
    if data[col].dtype in [np.float64, np.int64]:
        data[col].fillna(data[col].median(), inplace=True)
    else:
        data[col].fillna("Unknown", inplace=True)
anonymized_data = data.copy()

# 3. Ensure correct data types
numeric_cols = ["amt", "lat", "long", "merch_lat", "merch_long"]
for col in numeric_cols:
    anonymized_data[col] = pd.to_numeric(anonymized_data[col], errors='coerce')
    anonymized_data[col].fillna(anonymized_data[col].median(), inplace=True)

# -----------------------------
# Anonymization Functions
# -----------------------------
def mask_column(column):
    return ["XXXXXX" for _ in column]

def generalize_column(column, range_size):
    return [f"{(int(val)//range_size)*range_size}-{((int(val)//range_size)+1)*range_size -1}" for val in column]

def add_noise(column, noise_level=0.1):
    return [val + val * random.uniform(-noise_level, noise_level) for val in column]

# -----------------------------
# Columns to Anonymize
# -----------------------------
sensitive_cols = ["cc_num", "first", "last", "trans_num"]
generalize_cols = {"amt": 10}
continuous_cols = ["lat", "long", "merch_lat", "merch_long"]

# -----------------------------
# Apply Anonymization
# -----------------------------
for col in sensitive_cols:
    anonymized_data[col] = mask_column(anonymized_data[col])

for col, rng in generalize_cols.items():
    anonymized_data[col] = generalize_column(anonymized_data[col], rng)

for col in continuous_cols:
    anonymized_data[col] = add_noise(anonymized_data[col], noise_level=0.1)

# -----------------------------
# Pre- and Post-Anonymization Analysis
# -----------------------------
print("=== Pre and Post Anonymization Statistics ===")
for col in generalize_cols.keys() | set(continuous_cols):
    print(f"\nColumn: {col}")
    print("Before:\n", data[col].describe())
    print("After:\n", anonymized_data[col].describe())

# -----------------------------
# Privacy Metrics
# -----------------------------
print("\n=== Privacy Metrics ===")
for col in sensitive_cols + list(generalize_cols.keys()):
    original_unique = data[col].nunique()
    anonymized_unique = anonymized_data[col].nunique()
    reduction = ((original_unique - anonymized_unique) / original_unique) * 100
    print(f"{col} - Unique Values Reduced: {reduction:.2f}%")

for col in generalize_cols.keys():
    counts = anonymized_data.groupby(col).size()
    k_value = counts.min()
    print(f"{col} - k-anonymity (smallest group size): {k_value}")

for col in continuous_cols:
    corr = np.corrcoef(data[col], anonymized_data[col])[0,1]
    print(f"{col} - Correlation between original and anonymized: {corr:.2f}")

# -----------------------------
# Visualizations
# -----------------------------
for col in continuous_cols + list(generalize_cols.keys()):
    plt.figure(figsize=(6,4))
    plt.hist(data[col], bins=20, alpha=0.5, label="Original")
    plt.hist(anonymized_data[col], bins=20, alpha=0.5, label="Anonymized")
    plt.title(f"{col} - Original vs Anonymized")
    plt.legend()
    plt.show()

# -----------------------------
# Save Anonymized Dataset
# -----------------------------
output_path = "results/anonymized_credit_data.csv"
anonymized_data.to_csv(output_path, index=False)
print(f"\nAnonymized dataset saved to {output_path}")
