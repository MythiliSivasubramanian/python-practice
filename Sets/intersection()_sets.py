# Sets Intersection:
# Students in both morning and evening batches


morning_batch = {"Rose", "Anu", "Ravi", "John"}
evening_batch = {"John", "Meera", "Rose", "Kiran"}

# Students in both morning and evening batches
both_batches = morning_batch.intersection(evening_batch)

# Printing Morning batch students, evening batch students, and students in both batches
print("\n Morning Batch : ", morning_batch)
print("\n Evening Batch : ", evening_batch)
print("\n Students in both batches : ", both_batches)
print("\n Count of students in both batches : ", len(both_batches),"\n")
