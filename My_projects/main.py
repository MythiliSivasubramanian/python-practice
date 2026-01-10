import linecache

# Opening the raw student data file
f = open("/Users/aravinthmythili/Desktop/Github_Mythili_Sivasubramanian/python-practice/My_projects/raw_data.csv")
header = (f.readline())
data = f.readlines()
print(header)
print("\n\n",data[2:4])

lines = linecache.getline("/Users/aravinthmythili/Desktop/Github_Mythili_Sivasubramanian/python-practice/My_projects/raw_data.csv",2)
print(lines)