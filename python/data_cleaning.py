
import pandas as pd
import numpy as np
from pathlib import Path

# Project Main Folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset File Path
file_path = BASE_DIR / "Dataset" / "Sample_Superstore.csv"

# Load Dataset
df = pd.read_csv(file_path, encoding="latin1")

print("Dataset Loaded Successfully!")
print(df.head())


# Step 7: Explore Dataset

print("\nFirst 5 Rows:")
print(df.head())

print("\nTotal Rows and Columns:")
print(df.shape)

print("\nAll Column Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())


# Step 8: Check Missing Values

print("\nMissing Values in Dataset:")
print(df.isnull().sum())


# Step 9: Check Duplicate Records

print("\nDuplicate Records:")
print(df.duplicated().sum())


# Step 7: Convert Date Columns

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%m/%d/%Y",
    errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    format="%m/%d/%Y",
    errors="coerce"
)

print("\nDate Columns Converted Successfully!")
print(df[["Order Date", "Ship Date"]].head())


# Step 8: Clean Column Names

df.columns = df.columns.str.strip()

print("\nColumn Names Cleaned!")
print(df.columns.tolist())


# Step 9: Check Data Types

print("\nUpdated Data Types:")
print(df.dtypes)

# Step 10: Save Cleaned Dataset
BASE_DIR = Path(__file__).resolve().parent.parent
cleaned_file_path = BASE_DIR / "Dataset" / "Cleaned_Sample_Superstore.csv"
df.to_csv(cleaned_file_path, index=False, encoding="utf-8")        
print("\nData Cleaning Completed Successfully!")
print("Cleaned File Saved At:", cleaned_file_path)

print("\nFinal Dataset Shape:", df.shape)         