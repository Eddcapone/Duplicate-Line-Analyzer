# Duplicate Line Analyzer

## Overview
This Python script efficiently analyzes lines from a provided text file to identify and count duplicate entries. It's designed to help database administrators, developers and data analysts quickly understand the frequency of repeated lines in their logs, which can be critical for performance tuning and debugging. The script features functionality to filter and format the output based on line character length and to display results in a neatly formatted table.

## Features
- **Duplicate Counting:** Identify and count duplicate SQL query lines.
- **Character Filtering:** Include only lines that meet specified minimum and maximum character lengths.
- **Progress Bar:** Visual progress indicator for processing large files.
- **Formatted Output:** Results are displayed in a table format for easy readability.

## Prerequisites
Before you can run the script, you need Python installed on your machine. This script is compatible with Python 3.6 and above. Additionally, you need to install a couple of Python libraries:

- `pandas`: For organizing the data into a structured format.
- `tqdm`: For showing a progress bar during file processing.
- `tabulate`: For formatting the output in a table view.

You can install these dependencies via pip:

```bash
pip install pandas tqdm tabulate
```

## Installation
Clone this repository or download the script directly. If you choose to clone:

```bash
git clone https://yourgithubrepo.com/yourusername/duplicate-sql-query-analyzer.git
cd duplicate-sql-query-analyzer
```

## Usage
Run the script from the command line, providing the path to your file and other parameters as shown below:

```bash
python count_duplicates.py <file_path> <top_n> <max_chars> <min_chars>
```

### Arguments
<file_path>: Path to the SQL file to analyze.
<top_n>: The number of top duplicate queries to display.
<max_chars>: Maximum character length for each line to be included in the output.
<min_chars>: Minimum character length for each line to be included in the analysis.

#### Example
To analyze the top 10 duplicate queries in your_file_path.sql, considering lines between 50 and 100 characters:

```bash
python count_duplicates.py your_file_path.sql 10 100 50
```

## Output
The output will be displayed in your command line interface as a table with two columns: SQL Query and Count, representing the query and its frequency, respectively.

## Contributing
Contributions are welcome! Please feel free to submit pull requests, create issues for bugs and feature requests, or provide feedback.

## License
This project is open source and available under the MIT License.

## Credits
Written with the help of GPT-4
