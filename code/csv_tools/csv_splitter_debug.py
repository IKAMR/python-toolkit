import os
import csv
import argparse
from datetime import datetime

# Metadata
__version__ = "1.0.1"
__date__ = "2025-01-22"

def split_csv(input_file, output_folder, max_size=None, max_rows=None, ext_col=None, ext_list=None, prefix="split", log_file=None):
    """
    Extended CSV splitting tool with support for file extensions filtering.

    Parameters:
    input_file (str): Path to the source CSV file.
    output_folder (str): Target folder for output files.
    max_size (int, optional): Maximum size in bytes for each split file.
    max_rows (int, optional): Maximum number of rows per split file.
    ext_col (int, optional): Column index (0-based) containing file extensions.
    ext_list (list, optional): List of specific extensions to filter (e.g., ["txt", "xml"]).
    prefix (str, optional): Prefix for the split file names.
    log_file (str, optional): Path to the log file.
    """
    start_time = datetime.now()
    print(f"Starting CSV Splitter (v{__version__}, {__date__})")
    print(f"Start time: {start_time}")

    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found.")

    if not output_folder:
        output_folder = os.path.dirname(input_file)

    os.makedirs(output_folder, exist_ok=True)

    # Generate log file name if not provided
    if not log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
        log_file = os.path.join(output_folder, f"csv_splitter_{timestamp}.log")

    log_counter = 1
    while os.path.exists(log_file):
        log_file = os.path.join(output_folder, f"csv_splitter_{timestamp}_{log_counter}.log")
        log_counter += 1

    with open(log_file, 'w', encoding='utf-8') as log:
        log.write("CSV Splitting Log\n")
        log.write(f"Version: {__version__}, Date: {__date__}\n")
        log.write(f"Start time: {start_time}\n")

        try:
            with open(input_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                header = next(reader)

                log.write("Debugging first 20 rows:\n")
                row_count = 0

                for row in reader:
                    if row_count >= 20:
                        log.write("Stopping after debugging 20 rows.\n")
                        break

                    ext_value = None
                    if ext_col is not None:
                        ext_value = os.path.splitext(row[ext_col].strip().lower())[1].lstrip(".")
                    
                    log.write(f"Row {row_count + 1}: {row}\n")
                    log.write(f"Extracted extension: {ext_value}\n")

                    if ext_list:
                        match_status = ext_value in ext_list
                        log.write(f"Extension in list: {match_status}\n")
                    else:
                        log.write("Extension list not provided.\n")

                    row_count += 1

        except Exception as e:
            log.write(f"An error occurred: {e}\n")
            raise

        finally:
            end_time = datetime.now()
            log.write(f"End time: {end_time}\n")
            print(f"End time: {end_time}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extended CSV splitting tool.")
    parser.add_argument("input", type=str, help="Path to the input CSV file")
    parser.add_argument("output", type=str, help="Folder to save the output CSV files")
    parser.add_argument("--size", type=str, help="Maximum file size for split files (e.g., 500, 50kB, 200MB, 1GB)")
    parser.add_argument("--rows", type=int, help="Maximum number of rows per split file")
    parser.add_argument("--extcol", type=int, help="Column index (0-based) containing file extensions")
    parser.add_argument("--extlist", type=str, help="Comma-separated list of extensions to filter (e.g., 'txt,xml')")
    parser.add_argument("--log", type=str, help="Path to the log file")

    args = parser.parse_args()

    # Convert size to bytes
    size_mapping = {"kB": 1024, "MB": 1024**2, "GB": 1024**3}
    max_size = None
    if args.size:
        unit = args.size[-2:]
        if unit in size_mapping:
            max_size = int(args.size[:-2]) * size_mapping[unit]
        else:
            max_size = int(args.size)

    split_csv(
        input_file=args.input,
        output_folder=args.output,
        max_size=max_size,
        max_rows=args.rows,
        ext_col=args.extcol,
        ext_list=args.extlist,
        log_file=args.log
    )
