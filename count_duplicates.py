import argparse
import pandas as pd
from collections import Counter
import os
from tqdm import tqdm
from tabulate import tabulate
import re

def count_duplicate_lines(file_path, top_n, max_chars, min_chars, exclude_pattern=None, min_count=1):
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_rows', None)

    file_size = os.path.getsize(file_path)

    lines = []

    with open(file_path, 'r') as file:
        progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, desc="Processing file")
        while True:
            line = file.readline()
            if not line:
                break
            progress_bar.update(len(line.encode('utf-8')))
            stripped_line = line.strip()
            if stripped_line and len(stripped_line) >= min_chars and (exclude_pattern is None or not re.search(exclude_pattern, stripped_line)):
                lines.append(stripped_line[:max_chars])
        progress_bar.close()

    line_counts = Counter(lines)
    df = pd.DataFrame(list(line_counts.items()), columns=['Line', 'Count'])
    df.sort_values(by='Count', ascending=False, inplace=True)

    # Filter the DataFrame to include only lines with counts >= min_count
    filtered_df = df[df['Count'] >= min_count]

    return filtered_df.head(top_n)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count duplicate lines in a file with optional regex and count exclusion.')
    parser.add_argument('file_path', type=str, help='Path to the text file.')
    parser.add_argument('top_n', type=int, help='Number of top results to display.')
    parser.add_argument('max_chars', type=int, help='Maximum number of characters per line to consider.')
    parser.add_argument('min_chars', type=int, help='Minimum number of characters a line must contain to be considered.')
    parser.add_argument('--exclude', type=str, default=None, help='Regex pattern to exclude lines that match.')
    parser.add_argument('--min-count', type=int, default=1, help='Minimum count a line must have to be included in the results.')

    args = parser.parse_args()
    df = count_duplicate_lines(args.file_path, args.top_n, args.max_chars, args.min_chars, args.exclude, args.min_count)
    
    print(tabulate(df, headers='keys', tablefmt='psql'))
