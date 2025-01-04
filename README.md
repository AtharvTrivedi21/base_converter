# Base Converter with Constraints

**Base Converter with Constraints** is a Python package that allows users to perform base conversions while enforcing specific constraints on the converted representation. This package supports:

- Arbitrary base conversions (e.g., base 10 to base 6, base 16 to base 2).
- Constraints like:
  - Digit sum requirements.
  - Allowed and disallowed digits.
  - Palindrome patterns.

## Features

- Convert numbers between bases seamlessly.
- Enforce constraints to customize the converted representation.
- Supports advanced use cases like cryptography, encoding, and mathematical explorations.

## Installation

To install the package locally:

```bash
pip install base_converter
```

Or, if testing from source:

```bash
pip install dist/base_converter-0.1.0.tar.gz
```

## Usage

Here's an example of how to use the package:

```python
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
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
