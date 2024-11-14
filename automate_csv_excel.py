import pandas as pd
import os
import glob

# Merge multiple CSV files
def merge_csv_files(input_folder, output_file):
    csv_files = glob.glob(os.path.join(input_folder, "*.csv"))
    merged_df = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index=True)
    merged_df.to_csv(output_file, index=False)
    print(f"Merged CSV saved to {output_file}")

# Clean data by removing duplicates and NaN values
def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

# Generate a summary report in Excel format
def generate_summary(input_file, output_file):
    df = pd.read_csv(input_file)
    summary = df.describe() 
    summary.to_excel(output_file)
    print(f"Summary report saved to {output_file}")

# Test case:
if __name__ == "__main__":
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    print("Merging CSV files...")
    merge_csv_files("data", "output/merged_data.csv")

    print("Cleaning data...")
    clean_data("output/merged_data.csv", "output/cleaned_data.csv")

    print("Generating summary report...")
    generate_summary("output/cleaned_data.csv", "output/summary_report.xlsx")
