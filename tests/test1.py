from base_converter.converter import convert_with_constraints

# Convert number 345 from base 10 to base 6 with constraints
result = convert_with_constraints(
    number=345,
    source_base=10,
    target_base=6,
    constraints={
        "digit_sum": 10,
        "allowed_digits": [0, 1, 2, 3, 4]
    }
)
print("Valid Representations:", result)
