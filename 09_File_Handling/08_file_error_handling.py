# 08_file_error_handling.py
# Basic file error handling in Python 

import json

# 1) Read a text file safely

def read_text_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"SUCCESS: '{file_name}' read successfully")
            print(content)

    except FileNotFoundError:
        print(f"ERROR: '{file_name}' not found")

    except PermissionError:
        print(f"ERROR: No permission to read '{file_name}'")

    except UnicodeDecodeError:
        print(f"ERROR: Data in '{file_name}' is not readable as UTF-8 text")

    except Exception as e:
        print(f"ERROR: Something unexpected happened while reading '{file_name}' -> {e}")


# 2) Write a text file safely
def write_text_file(file_name, text):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"SUCCESS: '{file_name}' written successfully")

    except PermissionError:
        print(f"ERROR: No permission to write '{file_name}'")

    except Exception as e:
        print(f"ERROR: Something unexpected happened while writing '{file_name}' -> {e}")


# 3) Read JSON file safely
def read_json_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        print(f"SUCCESS: JSON from '{file_name}' -> {data}")

    except FileNotFoundError:
        print(f"ERROR: JSON file '{file_name}' not found")

    except json.JSONDecodeError:
        print(f"ERROR: '{file_name}' has invalid JSON format")

    except PermissionError:
        print(f"ERROR: No permission to read '{file_name}'")

    except Exception as e:
        print(f"ERROR: Something unexpected happened while reading JSON '{file_name}' -> {e}")


# Basic workouts

print("\nWorkout 1: File not found")
read_text_file("missing.txt")

print("\nWorkout 2: Successful write and read")
write_text_file("basic_demo.txt", "Line 1\nLine 2\n")
read_text_file("basic_demo.txt")

print("\nWorkout 3: Data not readable (UnicodeDecodeError)")
with open("not_readable.bin", "wb") as file:
    # Writing binary bytes that are not valid utf-8 text
    file.write(b"\xff\xfe\xfa")
read_text_file("not_readable.bin")

print("\nWorkout 4: Invalid JSON")
write_text_file("bad.json", '{"name": "Rose", "score": 95,}')
read_json_file("bad.json")

print("\nWorkout 5: Valid JSON")
write_text_file("good.json", '{"name": "John", "score": 90}')
read_json_file("good.json")

