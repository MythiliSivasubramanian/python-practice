"""
Topic  : Dictionaries
Task   : Survey Response Counter
Skills : Counting, probability ratio, classification
"""

"""
Task: “Survey Response Counter”
You conducted a small survey.
People answered: “Do you like Data Science?” → Yes / No
Here’s the raw response list. 
responses = ["Yes", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "No"]

"""

# Task 1 — Count Yes & No using Dictionary
# Create a dictionary with keys as "Yes" and "No" with default values as 0
result = dict.fromkeys(["Yes","No"],0)

# Raw response list(predefined)
responses = ["Yes", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "No"]

# Loop through the list response and update the result dictionary
for response in responses:
    if response == "Yes":
     result["Yes"] += 1
    if response == "No":
      result["No"] += 1

# Print the updated result
print("\n\nSurvey count :", result)

"""
Task 2 — Using the counts:Calculate Probabilities 
Formula: Probability = Count / Total responses.  Round to 2 decimals.
Create output like:
Probability of Yes : 0.60 Probability of No  : 0.40
"""

# Calculate Probability . Probability = Count / Total responses.
probability_yes = result["Yes"]/len(responses) 
probability_no = result["No"]/len(responses) 

print(f"\nProbability of Yes : {probability_yes:.2f}") # Round to 2 decimals
print(f"Probability of No : {probability_no:.2f}") # Round to 2 decimals

"""
Task 3 — Print Majority Decision. Survey Positive, Survey Negative, Survey Neutral.
"""
majority = ""
if result["Yes"] > result["No"]:
    majority = "Survey Positive"
elif result["No"] > result["Yes"]:
    majority = "Survey Negative"
elif result["Yes"] == result["No"]:
    majority = "Survey Neutral"

print("\nFinal Decision :",majority)
print('-' * 50)