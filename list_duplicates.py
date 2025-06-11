# GitHub: https://github.com/Eddcapone/Duplicate-Line-Analyzer

import argparse
import pandas as pd
from collections import Counter
import os
from tqdm import tqdm
from tabulate import tabulate
import re

# Strip timestamps like [2025-06-11T14:23:45.123456+02:00]
DATE_PATTERN = re.compile(r'\[\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}\]')

def count_duplicate_lines(file_path, top_n, max_chars, min_chars,
                          exclude_pattern=None, include_pattern=None,
                          min_count=1):
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_rows', None)

    file_size = os.path.getsize(file_path)
    lines = []

    with open(file_path, 'r') as file:
        progress_bar = tqdm(total=file_size,
                            unit='B', unit_scale=True,
                            desc="Processing file")
        while True:
            line = file.readline()
            if not line:
                break
            progress_bar.update(len(line.encode('utf-8')))

            # 1) Trim whitespace
            stripped_line = line.strip()
            # 2) Remove the date portion before any other checks
            cleaned_line = DATE_PATTERN.sub('', stripped_line)  # strip dates via re.sub :contentReference[oaicite:2]{index=2}

            # 3) Apply length and include/exclude filters
            if cleaned_line and len(cleaned_line) >= min_chars:
                if include_pattern and not re.search(include_pattern, cleaned_line):
                    continue
                if exclude_pattern and re.search(exclude_pattern, cleaned_line):
                    continue
                # 4) Truncate to max_chars and collect
                lines.append(cleaned_line[:max_chars])
        progress_bar.close()

    # Count duplicates
    line_counts = Counter(lines)
    df = pd.DataFrame(line_counts.items(), columns=['Line', 'Count'])
    df.sort_values(by='Count', ascending=False, inplace=True)

    # Only keep those with at least min_count occurrences
    filtered_df = df[df['Count'] >= min_count]

    return filtered_df.head(top_n)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Count duplicate lines in a file with optional regex inclusion/exclusion, stripping timestamps.')
    parser.add_argument('file_path', type=str,
                        help='Path to the text file.')
    parser.add_argument('top_n', type=int,
                        help='Number of top results to display.')
    parser.add_argument('max_chars', type=int,
                        help='Maximum number of characters per line to consider.')
    parser.add_argument('min_chars', type=int,
                        help='Minimum number of characters a line must contain to be considered.')
    parser.add_argument('--exclude', type=str, default=None,
                        help='Regex pattern to exclude lines that match.')
    parser.add_argument('--include', type=str, default=None,
                        help='Regex pattern to include only lines that match.')
    parser.add_argument('--min-count', type=int, default=1,
                        help='Minimum count a line must have to be included in the results.')

    args = parser.parse_args()
    df = count_duplicate_lines(
        args.file_path, args.top_n, args.max_chars,
        args.min_chars, args.exclude, args.include,
        args.min_count
    )
    print(tabulate(df, headers='keys', tablefmt='psql'))
