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
"""
CARD 3:
    Splits a full name into (first_name, last_name).
    Assumption: name is 'First Last'. If missing parts -> 'Unknown'.
    """

def split_name(full_name):
    
    full_name = collapse_spaces(full_name)

    if not full_name:
        return "Unknown", "Unknown"

    parts = full_name.split()

    first = parts[0].capitalize() if parts[0] else "Unknown"
    last = parts[1].capitalize() if len(parts) > 1 and parts[1] else "Unknown"

    return first, last


def clean_marks(marks_text):
    """
    Converts marks to float and rounds to 2 decimals.
    Missing/invalid -> 0.0
    """
    marks_text = collapse_spaces(marks_text)

    if not marks_text:
        return 0.0

    try:
        return round(float(marks_text), 2)
    except ValueError:
        return 0.0


def clean_year(year_text):
    """
    Converts year to int if possible.
    Missing/invalid -> 'Unknown'
    """
    year_text = collapse_spaces(year_text)

    if not year_text:
        return "Unknown"

    try:
        return int(year_text)
    except ValueError:
        return "Unknown"


def apply_defaults(normalized_fields):
    """
    Takes normalized fields [name, subject, marks, year] and applies:
    - Name split + Unknown defaults
    - Subject default
    - Marks conversion + default
    - Year conversion + default

    Returns a structured dict ready for next steps.
    """
    name, subject, marks, year = normalized_fields

    first_name, last_name = split_name(name)

    subject = normalize_subject(subject)
    if not subject:
        subject = "Unknown"

    marks = clean_marks(marks)
    year = clean_year(year)

    return {
        "First_Name": first_name,
        "Last_Name": last_name,
        "Subject": subject,
        "Marks": marks,
        "Year": year,
    }
"""
    Card 4: Remove duplicate records after normalization
    Removes duplicate student records.

    A duplicate is defined as having the same:
    First_Name, Last_Name, Subject, Marks, Year

    Keeps the first occurrence (stable order).
    """

def deduplicate_records(records):
   
    seen = set()
    unique = []

    for r in records:
        key = (r["First_Name"], r["Last_Name"], r["Subject"], r["Marks"], r["Year"])
        if key not in seen:
            seen.add(key)
            unique.append(r)

    return unique