# Function to calculate gross salary
def calculate_gross_salary(basic, grade):
    HRA = 0.20 * basic
    DA = 0.50 * basic

    if grade == 'A':
        Allow = 1700
    elif grade == 'B':
        Allow = 1500
    else:
        Allow = 1300

    PF = 0.11 * basic

    gross_salary = basic + HRA + DA + Allow - PF
    return gross_salary

# Input data
basic_A = 10000
grade_A = 'A'
basic_B = 4567
grade_B = 'B'

# Calculate gross salary for grade A and B
gross_salary_A = calculate_gross_salary(basic_A, grade_A)
gross_salary_B = calculate_gross_salary(basic_B, grade_B)

# Display results
print("Gross Salary for Grade A:", gross_salary_A)
print("Gross Salary for Grade B:", gross_salary_B)
