# Count unique website visitors

day1_visitors = {"ip1", "ip2", "ip3", "ip4"}
day2_visitors = {"ip3", "ip4", "ip5", "ip6"}

unique_visitors = day1_visitors | day2_visitors

print("\nDay 1 : ", day1_visitors)
print("\nDay 2 : ", day2_visitors)
print("\nTotal unique visitors : ", unique_visitors)
print("\nCount : ", len(unique_visitors))