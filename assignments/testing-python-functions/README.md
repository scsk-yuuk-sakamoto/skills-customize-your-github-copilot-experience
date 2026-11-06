# 📘 Assignment: Testing Python Functions with pytest

## 🎯 Objective

Write and run tests for Python functions using pytest. Practice checking expected results with assertions and choosing inputs that cover typical and boundary cases.

## 📝 Tasks

### 🛠️ Write Tests for Addition

#### Description
Install pytest with `python -m pip install pytest`, then create a test file named `test_starter_code.py` for the provided `add` function.

#### Requirements
Completed tests should:

- Import `add` from `starter_code.py`.
- Include a test function that checks adding two positive integers.
- Use `assert` to check the expected result for adding zero and a negative integer.
- Pass when run with `pytest -q` from the assignment folder.

### 🛠️ Test Even and Odd Numbers

#### Description
Add tests for the provided `is_even` function, including zero and negative numbers, and run the complete test suite.

#### Requirements
Completed tests should:

- Import `is_even` from `starter_code.py`.
- Check that a positive even number and zero return `True`.
- Check that a positive odd number and a negative odd number return `False`.
- Pass together with the `add` tests when run with `pytest -q`.