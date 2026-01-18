# Check if two sets have no common elements

group_A = {"red", "green", "blue"}
group_B = {"yellow", "purple"}

if group_A.isdisjoint(group_B):
    print("No common elements between the groups")
else:
    print("Groups share some elements")
