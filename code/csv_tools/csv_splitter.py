import os
import csv
import argparse
from datetime import datetime

# Metadata
__version__ = "1.0.0"
__date__ = "2025-01-22"

def split_csv(input_file, output_folder, max_size=None, max_rows=None, column_index=None, prefix="split", log_file=None): 
    """
    General CSV splitting tool.
    - Split by file size
    - Split by specific column value or inferred file extension
    - Split by a maximum number of rows
    - Combine multiple splitting criteria

    Parameters:
    input_file (str): Path to the source CSV file.
    output_folder (str): Target folder for output files.
    max_size (int, optional): Maximum size in bytes for each split file.
    max_rows (int, optional): Maximum number of rows per split file.
    column_index (int, optional): For split by column value or file extension.
    prefix (str, optional): Prefix for the split file names.
    log_file (str, optional): Path to the log file.
    """
    start_time = datetime.now()
    print(f"Start time: {start_time}")

    if not os.path.isfile(input_file):
        error_message = f"Error: The input path '{input_file}' must be a valid file, not a folder."
        print(error_message)
        if log_file:
            with open(log_file, 'a', encoding='utf-8') as log:
                log.write(error_message + "\n")
        raise FileNotFoundError(error_message)

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
        log.write(f"CSV Splitting Log\nStart time: {start_time}\n")

        try:
            with open(input_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                header = next(reader)

                if column_index is not None:
                    column_groups = {}

                    for row in reader:
                        key = row[column_index].strip()
                        if not key:
                            raise ValueError("Empty key found in the specified column.")
                        column_groups.setdefault(key, []).append(row)

                    for key, rows in column_groups.items():
                        sanitized_key = key.replace('.', '').replace('/', '_')
                        file_count = 1
                        current_size = 0
                        current_rows = 0

                        output_file = os.path.join(output_folder, f"{prefix}_{sanitized_key}_{file_count}.csv")
                        output_file_handle = open(output_file, 'w', encoding='utf-8', newline='')
                        writer = csv.writer(output_file_handle)
                        writer.writerow(header)

                        for row in rows:
                            writer.writerow(row)
                            output_file_handle.flush()
                            current_size = os.path.getsize(output_file)
                            current_rows += 1

                            if (max_size and current_size >= max_size) or (max_rows and current_rows >= max_rows):
                                output_file_handle.close()
                                log.write(f"Created file: {output_file}\n")
                                file_count += 1
                                current_size = 0
                                current_rows = 0
                                output_file = os.path.join(output_folder, f"{prefix}_{sanitized_key}_{file_count}.csv")
                                output_file_handle = open(output_file, 'w', encoding='utf-8', newline='')
                                writer = csv.writer(output_file_handle)
                                writer.writerow(header)

                        output_file_handle.close()
                        log.write(f"Created file: {output_file}\n")

                elif max_size or max_rows:
                    current_size = 0
                    current_rows = 0
                    file_count = 1
                    output_file = os.path.join(output_folder, f"{prefix}_{file_count}.csv")
                    output_file_handle = open(output_file, 'w', encoding='utf-8', newline='')
                    writer = csv.writer(output_file_handle)
                    writer.writerow(header)

                    for row in reader:
                        writer.writerow(row)
                        output_file_handle.flush()
                        current_size = os.path.getsize(output_file)
                        current_rows += 1

                        if (max_size and current_size >= max_size) or (max_rows and current_rows >= max_rows):
                            output_file_handle.close()
                            log.write(f"Created file: {output_file}\n")
                            file_count += 1
                            current_size = 0
                            current_rows = 0
                            output_file = os.path.join(output_folder, f"{prefix}_{file_count}.csv")
                            output_file_handle = open(output_file, 'w', encoding='utf-8', newline='')
                            writer = csv.writer(output_file_handle)
                            writer.writerow(header)

                    output_file_handle.close()
                    log.write(f"Created file: {output_file}\n")

                else:
                    raise ValueError("Either max_size, max_rows, or column_index must be specified.")

        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(error_message)
            log.write(error_message + "\n")
            raise

        finally:
            end_time = datetime.now()
            log.write(f"End time: {end_time}\n")
            print(f"End time: {end_time}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flexible CSV splitting tool.")
    parser.add_argument("input", type=str, help="Path to the input CSV file")
    parser.add_argument("output", type=str, help="Folder to save the output CSV files")
    parser.add_argument("--size", type=str, help="Maximum file size for split files (e.g., 500, 50kB, 200MB, 1GB)")
    parser.add_argument("--rows", type=int, help="Maximum number of rows per split file")
    parser.add_argument("--ext", type=int, help="Column index to use for file extension grouping")
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
            # Assume bytes if no unit is provided
            max_size = int(args.size)

    split_csv(args.input, args.output, max_size=max_size, max_rows=args.rows, column_index=args.ext, log_file=args.log)
