# Duplicate Line Analyzer

## Overview
This Python script efficiently analyzes lines from a provided text file to identify and count duplicate entries. It's designed to help database administrators, developers, and data analysts quickly understand the frequency of repeated lines in their logs, which can be critical for performance tuning and debugging. The script now includes functionality to exclude specific lines based on a regex pattern, in addition to filtering and formatting the output based on line character length.

## Features
- **Duplicate Counting:** Identify and count duplicate lines.
- **Character Filtering:** Include only lines that meet specified minimum and maximum character lengths.
- **Regex Exclusion:** Exclude lines that match a specified regex pattern.
- **Progress Bar:** Visual progress indicator for processing large files.
- **Formatted Output:** Results are displayed in a table format for easy readability.

## Prerequisites
Before you can run the script, you need Python installed on your machine. This script is compatible with Python 3.6 and above. Additionally, you need to install a couple of Python libraries:

- `pandas`: For organizing the data into a structured format.
- `tqdm`: For showing a progress bar during file processing.
- `tabulate`: For formatting the output in a table view.
- `argparse`: For parsing command-line options and arguments.

You can install these dependencies via pip:

```bash
pip install pandas tqdm tabulate argparse
```

## Installation
Clone this repository or download the script directly. If you choose to clone:

```bash
git clone https://yourgithubrepo.com/yourusername/duplicate-line-analyzer.git
cd duplicate-line-analyzer
```

## Usage
Run the script from the command line, providing the path to your file and other parameters as shown below:

```bash
python count_duplicates.py <file_path> <top_n> <max_chars> <min_chars> [--exclude PATTERN]
```

## Arguments

```vbnet
<file_path>: Path to the file to analyze.
<top_n>: The number of top duplicate lines to display.
<max_chars>: Maximum character length for each line to be included in the output.
<min_chars>: Minimum character length for each line to be included in the analysis.

Optional:
--exclude PATTERN: Optional regex pattern to exclude lines that match.
--include PATTERN: Optional regex pattern to include lines that match.
--min-count: Minimum count a line must have to be included in the results.
--help: Shows Manual
```

## Examples

This command will analyze *your_file.txt* and print out the top 10 lines with the most duplicates, considering lines that are at least 20 characters long and truncating them to 100 characters if they are longer and excluding lines containing the word "error":

```bash
python count_duplicates.py your_file.txt 10 100 20 --exclude "Megamenu"
```

![image](https://github.com/Eddcapone/Duplicate-Line-Analyzer/assets/16349349/423c0ae7-e207-4d6d-95d4-5559edbb4712)

-------------

This command will analyze *your_file.txt* and print out the top 10 lines with the most duplicates, considering lines that are at least 20 characters long and truncating them to 100 characters if they are longer and only including lines containing the word "SQL" and only shows results with a count greater than 10.

```bash
python count_duplicates.py your_file.txt 10 100 20 --include="Framework" --min-count=10
```
![image](https://github.com/Eddcapone/Duplicate-Line-Analyzer/assets/16349349/78e7c28d-a0fa-430b-b531-54be6fc5bbfd)



## Contributing
Contributions are welcome! Please feel free to submit pull requests, create issues for bugs and feature requests, or provide feedback.

## License
This project is open source and available under the MIT License.

## Credits
Written with the help of ChatGPT-4
