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

"""
   Card 2:  Parses a single raw input line into structured fields.

    What this function DOES:
    - Splits the line using the given delimiter
    - Trims extra whitespace from each field
    - Ensures exactly `expected_fields` fields by padding with empty strings ("")
    - Ignores extra fields anything beyond the expected count
    - Returns: list[str]: A list of exactly `expected_fields` strings
"""
def parse_record(line, delimiter=",", expected_fields=4):
  
    # Handle empty or whitespace-only lines 
    if not line or not line.strip():
        return [""] * expected_fields

    # Step 1: split by delimiter
    fields = line.split(delimiter)

    # Step 2: trim whitespace from each field
    fields = [field.strip() for field in fields]

    # Step 3: ensure fixed number of fields
    if len(fields) < expected_fields:
        fields.extend([""] * (expected_fields - len(fields)))
    else:
        fields = fields[:expected_fields]

    return fields
def collapse_spaces(text):
    """
    Collapses multiple internal whitespace into a single space.
    Also strips leading/trailing whitespace.
    Example: "  John   Doe  " -> "John Doe"
    """
    if text is None:
        return ""
    return " ".join(text.split())

"""
Card 3: Normalize casing and remove extra spaces
    Normalizes a name into proper case with single spaces.
    Example: "  jOhN   doE " -> "John Doe"
    Returns "" if input is empty/whitespace.
"""
def normalize_name(name):
  
    name = collapse_spaces(name)
    if not name:
        return ""
    return " ".join(part.capitalize() for part in name.split(" "))


def normalize_subject(subject):
    """
    Normalizes subject casing and spacing.
    Example: "  mAtH  " -> "Math"
    Returns "" if input is empty/whitespace.
    """
    subject = collapse_spaces(subject)
    if not subject:
        return ""
    return " ".join(word.capitalize() for word in subject.split(" "))


def normalize_fields(parsed_fields):
    """
    Takes [name, subject, marks, year] (all strings) and normalizes text fields.
    Marks/year are only space-collapsed here (no type conversion yet).
    Returns a list of 4 strings.
    """
    name, subject, marks, year = parsed_fields

    name = normalize_name(name)
    subject = normalize_subject(subject)

    # Keep marks/year as strings for now; just collapse spaces
    marks = collapse_spaces(marks)
    year = collapse_spaces(year)

    return [name, subject, marks, year]
