print("Hello World")
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
print(counties_tuple[1:2])
counties_dict = {
    'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
print(len(counties_dict))
print(counties_dict.keys())
voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})
print(voting_data)
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
