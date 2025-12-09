import pandas as pd
import os

def read_netflix_data(file_path='netflix_data.csv'):
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} was not found. Please make sure the file exists in the correct location.")

        # Read the CSV file
        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure that:")
        print("1. The CSV file is in the same directory as the script")
        print("2. The file name is correct (netflix_data.csv)")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Main execution
if __name__ == "__main__":
    df = read_netflix_data()
    if df is not None:
        print("Data loaded successfully!")
        # Continue with your analysis here