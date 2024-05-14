import pandas as pd
import numpy as np


def load_and_split_data(csv_file, x):
    # Load the data from a CSV file
    df = pd.read_csv(csv_file)

    # Calculate the number of rows each Parquet file should have
    rows_per_file = int(np.ceil(df.shape[0] / x))

    # Split the dataframe into x parts and save each as a Parquet file
    for i in range(x):
        start_idx = i * rows_per_file
        end_idx = start_idx + rows_per_file
        # Create a subset of the dataframe
        df_subset = df.iloc[start_idx:end_idx]
        # Save the subset to a Parquet file
        df_subset.to_parquet(f'{save_path}\data_part_{i + 1}.parquet')


# Example usage
csv_file_path = 'G:\Mon Drive\data\Vader.rescaled.data.csv.xls'  # Replace with your CSV file path
parts = 2  # Number of parts to split the CSV into
save_path = 'G:\Mon Drive\data'
load_and_split_data(csv_file_path, parts)