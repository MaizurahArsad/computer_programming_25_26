# Compound Interest Calculation

# Given values
principal_amount = 100        # initial money (RM)
annual_interest_rate = 5.0    # yearly interest rate (%)
number_of_years = 7           # time in years

# Calculate future value
future_value = principal_amount * \
    (1 + annual_interest_rate / 100) ** number_of_years

# Print result
print("Future value after", number_of_years,
      "years is: RM", round(future_value, 2))

string3 = """This is a
multiline string in Python"""

string4 = string3.lower()
print(string4)
