"""
    Reads a raw student data .txt file line-by-line.
    - Skips empty lines
    - Strips leading/trailing whitespaces
    - Returns a list of raw record strings for further parsing
    - Error message when file not found or other issues
"""


def read_raw_file(file_path):
    records = []

# Open and safely read the file line by line
    try:
        with open(file_path, "r") as f:
            for line in f: # streaming (Not to load entire file into memory)
                cleaned_line = line.strip()
                if cleaned_line:          # skip empty lines
                    # Return each line as string for further parsing
                    records.append(cleaned_line)
# Error message when file not found
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

# Generic error or runtime errors
    except Exception as e:
        print(f"Error while reading file: {e}")
        return []

    return records
