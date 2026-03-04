## IE7374 – MLOps Lab 1

This repository contains **Lab 1** for the course **IE7374: MLOps**.  
The project demonstrates foundational MLOps practices by building a simple Python calculator module and integrating it with testing and continuous integration workflows.

The lab focuses on setting up a clean Python project structure, implementing automated tests, and configuring **GitHub Actions** to validate code quality on every push.

---

## Project Overview

The purpose of this lab is to understand and apply core MLOps concepts in a practical development workflow.  
Although the example project is a lightweight calculator module, the real objective is to practice industry-relevant software engineering and MLOps foundations such as:

- organizing source code into a maintainable repository structure
- working with Python virtual environments
- writing automated tests using multiple testing frameworks
- setting up CI pipelines using GitHub Actions
- validating code changes automatically during development

---

## Objective

The main goals of this lab were to:

- create a structured Python project repository
- implement reusable calculator functions
- write automated test cases using both **Pytest** and **Unittest**
- configure **GitHub Actions** workflows for CI
- understand how automated testing supports reliable ML and software pipelines

---

## Project Structure

```bash
IE7374_MLOps_LAB1/
│── src/
│   ├── calculator.py
│   └── __init__.py
│
│── test/
│   ├── test_pytest.py
│   ├── test_unittest.py
│   └── __init__.py
│
│── .github/
│   └── workflows/
│       ├── pytest_action.yml
│       └── unittest_action.yml
│
│── requirements.txt
│── .gitignore
│── README.md

```

## Functionality

The `calculator.py` module contains the following functions:

- **fun1(x, y)** – Performs addition  
- **fun2(x, y)** – Performs subtraction  
- **fun3(x, y)** – Performs multiplication  
- **fun4(x, y)** – Performs a combination of arithmetic operations  
- **fun5(x, y)** – Performs division with error handling for divide-by-zero  

---

## Tools and Technologies Used

- **Python**
- **Pytest**
- **Unittest**
- **Git**
- **GitHub**
- **GitHub Actions**
- **Virtual Environments**

---

## Testing

This project uses two separate Python testing frameworks to validate the calculator module.

### 1. Pytest

Pytest is used to test all calculator functions in a concise and scalable format.

**Includes:**
- tests for all arithmetic functions
- **parameterized tests** for multiple input combinations
- cleaner and more flexible test design

### 2. Unittest

Unittest is used through the `unittest.TestCase` structure.

**Includes:**
- structured unit test methods
- coverage for all calculator functions
- validation of exception handling behavior

---

## Continuous Integration

This project includes **two GitHub Actions workflows** that run automatically on every push to the `main` branch.

### Configured Workflows

- **Testing with Pytest**
- **Python Unittests**

These workflows ensure that:
- code changes do not break existing functionality
- test cases run automatically in a clean environment
- the repository follows a basic CI pipeline setup

---

## Custom Modifications

To ensure the lab implementation is distinct and more complete, the following improvements were added:

- added a new division function: **fun5(x, y)**
- implemented divide-by-zero exception handling
- added **parameterized tests** in Pytest for broader input coverage
- expanded Unittest coverage to include error handling scenarios

---

## Key Learnings

Through this lab, I learned:

- how to structure a Python project for maintainability
- how to write and organize tests using both **Pytest** and **Unittest**
- how continuous integration works using **GitHub Actions**
- how automated validation improves reliability in software and MLOps workflows

---

## How to Run This Project

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd IE7374_MLOps_LAB1
```

### 2. Create a Virtual Environment

#### On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run the Tests

### Run Pytest

```bash
pytest
```

### Run Unittest

```bash
python -m unittest discover -s test
```

---

## Expected Outcome

After setup, the project should:

- run calculator functions successfully
- pass all Pytest test cases
- pass all Unittest test cases
- trigger GitHub Actions workflows automatically on push

---

## Why This Project Matters

While this lab uses a simple calculator example, it reflects key principles used in production-grade ML and software systems:

- modular code organization
- repeatable environments
- automated testing
- continuous integration
- disciplined repository management

These are foundational building blocks for larger MLOps pipelines and reliable deployment workflows.

---

## Author

**Fatima Zehrah**  
Master’s in Data Analytics Engineering  
Northeastern University

