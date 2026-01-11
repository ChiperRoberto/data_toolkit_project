import pandas as pd
import glob
import os


def load_and_standardize():
    """Load raw CSVs, standardize columns, and combine."""

    # Load 2022 Data
    df_22 = pd.read_csv("data/raw/records_2022.csv")
    # Fix Schema Drift: Rename 'source' to 'source_system'
    df_22 = df_22.rename(columns={"source": "source_system"})
    # Add missing columns in 2022 with None/NaN
    df_22["department"] = None
    df_22["priority"] = None

    # Load 2023 Data
    df_23 = pd.read_csv("data/raw/records_2023.csv")

    # Combine
    df = pd.concat([df_22, df_23], ignore_index=True)
    return df


def clean_data(df):
    """Apply cleaning logic to the combined dataframe."""

    # 1. Normalize Category Strings (strip whitespace, lowercase, fix typos)
    df['category'] = df['category'].astype(str).str.strip().str.lower()
    df['category'] = df['category'].replace({
        'labtest': 'lab_test',
        'follow-up': 'follow_up'
    })

    # 2. Normalize Source System & Status
    cols_to_lower = ['source_system', 'status', 'unit']
    for col in cols_to_lower:
        df[col] = df[col].astype(str).str.strip().str.lower()

    # 3. Handle Dates (Mixed Formats: YYYY-MM-DD and DD/MM/YYYY)
    # format='mixed' allows Pandas to handle both formats automatically
    df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True, errors='coerce')
    # 4. Handle Outliers (Negative values)
    # Assuming negative values in 'value' are data entry errors and should be positive
    df['value'] = df['value'].abs()

    # 5. Drop Duplicates
    df = df.drop_duplicates(subset=['record_id'], keep='last')

    return df


def generate_report(df):
    """Generate a simple summary report."""
    summary = df.groupby(['category', 'status']).size().unstack(fill_value=0)
    summary.to_csv("reports/summary_table.csv")
    print("Summary table saved to reports/summary_table.csv")


if __name__ == "__main__":
    print("Starting pipeline...")

    # Ensure directories exist
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    # Pipeline
    raw_df = load_and_standardize()
    clean_df = clean_data(raw_df)

    # Save Output (Task 6.7: Two formats)
    clean_df.to_csv("data/processed/records_clean.csv", index=False)
    clean_df.to_parquet("data/processed/records_clean.parquet", index=False)

    generate_report(clean_df)
    print("Pipeline finished. Data saved to data/processed/")