import argparse
import json
import pandas as pd
from src.did.modelling import calculate_did

def main():
    """
    Main function to run the DiD analysis.
    """
    parser = argparse.ArgumentParser(description="Calculate Difference-in-Differences.")
    parser.add_argument("file_path", type=str, help="Path to the input CSV file.")
    args = parser.parse_args()

    # Read the CSV file
    try:
        df = pd.read_csv(args.file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {args.file_path}")
        return
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    # Validate required columns
    required_columns = ['pre-period', 'treatment', 'target']
    if not all(col in df.columns for col in required_columns):
        print(f"Error: CSV file must contain columns: {', '.join(required_columns)}")
        return

    # Calculate DiD
    try:
        coefficient, p_value = calculate_did(df)
    except Exception as e:
        print(f"Error during DiD calculation: {e}")
        return

    # Store results in a dictionary
    results = {
        'did_coefficient': coefficient,
        'p_value': p_value
    }

    # Print results as JSON
    print(json.dumps(results))

if __name__ == "__main__":
    main()
