# IE7374_MLops_LAB1
# IE7374 – MLOps Lab 1

This repository contains **Lab 1** for the course **IE7374: MLOps**.  
The lab demonstrates core MLOps foundations including virtual environments, GitHub repositories, unit testing, and CI/CD using GitHub Actions.

---

## Project Structure

<img width="309" height="544" alt="image" src="https://github.com/user-attachments/assets/e00cfafe-5efa-47db-8893-9a10df03927f" />


---

## Functionality

The `calculator.py` module includes the following functions:

- `fun1(x, y)` – Addition  
- `fun2(x, y)` – Subtraction  
- `fun3(x, y)` – Multiplication  
- `fun4(x, y)` – Combination of arithmetic operations  
- `fun5(x, y)` – Division with error handling for divide-by-zero (**custom modification**)  

---

## Testing

Two testing frameworks are used:

### Pytest
- Tests all calculator functions
- Includes **parametrized tests** for multiple input scenarios (**custom modification**)

### Unittest
- Uses `unittest.TestCase`
- Covers all calculator functions including error handling

---

## Continuous Integration

Two GitHub Actions workflows are configured and triggered automatically on every push to `main`:

- **Testing with Pytest**
- **Python Unittests**

Both workflows pass successfully on GitHub Actions.

---

## Custom Modifications

To ensure the lab is not identical to the base repository:
- Added a new division function (`fun5`) with exception handling
- Added parametrized tests in Pytest
- Expanded Unittest coverage

