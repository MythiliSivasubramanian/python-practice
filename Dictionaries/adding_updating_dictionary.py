my_dict = {}
print(f"\nInitial my_dict : {my_dict} | Memory: {sys.getsizeof(my_dict)}")

# Method 1: Direct assignment (BEST & MOST COMMON)
my_dict["name"] = "Anna Maria"
print(f"After direct add : {my_dict} | Memory: {sys.getsizeof(my_dict)}")

# Method 2: Update existing key
my_dict["name"] = "Micky"
print(f"After update key : {my_dict}")

# Method 3: update() method (single / multiple)
my_dict.update(age=22, language="English, German")
print(f"After update() : {my_dict}")

# Method 4: setdefault() (adds only if key missing)
my_dict.setdefault("country", "Germany")
my_dict.setdefault("age", 30)  # will NOT overwrite
print(f"After setdefault() : {my_dict}")
