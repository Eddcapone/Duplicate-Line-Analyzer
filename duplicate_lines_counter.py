import pandas as pd
from collections import Counter
import sys
from tqdm import tqdm
import os
from tabulate import tabulate

def count_duplicate_lines(file_path, top_n, max_chars, min_chars):
    # Adjust display settings
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_rows', None)  # Optional: Adjust as needed to display more rows

    # Determine the size of the file for progress tracking
    file_size = os.path.getsize(file_path)

    # Initialize a list to hold non-empty lines that meet the minimum character requirement
    lines = []

    # Read all lines from the file, with progress bar
    with open(file_path, 'r') as file:
        # Initialize tqdm with the total file size for better accuracy
        progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, desc="Processing file")

        # Read line by line
        while True:
            line = file.readline()
            if not line:
                break  # End of file
            progress_bar.update(len(line.encode('utf-8')))  # Update progress bar by byte length of the read line
            stripped_line = line.strip()
            if stripped_line and len(stripped_line) >= min_chars:  # Only add lines meeting min_chars requirement
                lines.append(stripped_line[:max_chars])  # Truncate lines
        
        progress_bar.close()  # Close the progress bar after file read completion

    # Count occurrences of each line
    line_counts = Counter(lines)

    # Create a DataFrame to display results
    df = pd.DataFrame(list(line_counts.items()), columns=['SQL Query', 'Count'])

    # Sort by the count in descending order
    df.sort_values(by='Count', ascending=False, inplace=True)

    # Return only the top N results
    return df.head(top_n)

if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script_name.py <file_path> <top_n> <max_chars> <min_chars>")
        sys.exit(1)

    file_path = sys.argv[1]
    top_n = int(sys.argv[2])  # Convert the second argument to an integer for top N results
    max_chars = int(sys.argv[3])  # Convert the third argument to an integer for max characters per line
    min_chars = int(sys.argv[4])  # Convert the fourth argument to an integer for min characters per line
    df = count_duplicate_lines(file_path, top_n, max_chars, min_chars)
    
    # Print the DataFrame using tabulate for better formatting
    print(tabulate(df, headers='keys', tablefmt='psql'))
