
# Skip headerline (1st line) and print till EoF

# Opening the raw student data file using:  with open() as f:
# With open() as f automatically closes file after use
with open("/Users/aravinthmythili/Desktop/Github_Mythili_Sivasubramanian/python-practice/My_projects/raw_data.csv") as f:
    next(f) # Skips the 1st line : headerline
    for line in f:    # Prints until EOF
        print(line.strip())
        