# CSV Splitter Tool

## Description
The **CSV Splitter Tool** is a versatile Python script designed to split large CSV files into smaller, manageable parts. It supports splitting by:
- File size (e.g., 500 bytes, 50kB, 200MB, 1GB).
- Row count (e.g., maximum rows per file).
- Specific column values (e.g., grouping by file extensions).
- A combination of these criteria.

This tool is useful for handling large datasets, organizing data by categories, or preparing files for downstream processing.

---

## Features
- **Split by File Size**: Define the maximum file size, and the tool will split the input file accordingly.
- **Split by Row Count**: Specify the maximum number of rows per output file.
- **Split by Column Values**: Group rows by the values in a specific column (e.g., file extensions).
- **Combine Splitting Criteria**: Use any combination of file size, row count, and column-based grouping.
- **Logging**: Automatically logs operations, including start and end times, and details about created files.

---

## Usage
The script is executed via the command line with the following parameters:

### Parameters
| Parameter      | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `input`        | Path to the input CSV file (required). The file must exist.                |
| `output`       | Path to the folder where output files will be saved. Defaults to the input file's folder if not specified. |
| `--size`       | Maximum file size for splitting. Accepts values like `500`, `50kB`, `200MB`, `1GB`. |
| `--rows`       | Maximum number of rows per split file.                                     |
| `--ext`        | Column index (0-based) used to group rows by their values.                 |
| `--log`        | Path to the log file. Defaults to a timestamped log in the output folder.  |

---

### Examples

#### 1. **Split by File Size**
Split the input file into smaller files of 50kB each:
```bash
python csv_splitter.py "input.csv" "output_folder" --size 50kB
```

#### 2. **Split by Row Count**
Split the input file into files containing at most 100 rows each:
```bash
python csv_splitter.py "input.csv" "output_folder" --rows 100
```

#### 3. **Split by Column (e.g., File Extensions)**
Group rows by file extensions found in column 2:
```bash
python csv_splitter.py "input.csv" "output_folder" --ext 2
```

#### 4. **Combine File Size and Row Count**
Limit each file to at most 200MB and 500 rows:
```bash
python csv_splitter.py "input.csv" "output_folder" --size 200MB --rows 500
```

#### 5. **Custom Log File**
Specify a custom log file location:
```bash
python csv_splitter.py "input.csv" "output_folder" --size 50kB --log "custom_log.txt"
```

---

## Output
- **Split Files**: Files are named using the pattern `<prefix>_<key>_<counter>.csv`, where:
  - `<prefix>` is "split" by default.
  - `<key>` is the sanitized value of the specified column (if splitting by column).
  - `<counter>` increments for each split file.
- **Log File**: A detailed log of the operation is created in the output folder by default.

---

## Requirements
- Python 3.7+

Install any required dependencies:
```bash
pip install -r requirements.txt
```

---

## Notes
- Ensure the input file exists and the output folder is writable.
- If none of the options `--size`, `--rows`, or `--ext` are provided, the script will raise an error as at least one splitting criterion must be specified.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

