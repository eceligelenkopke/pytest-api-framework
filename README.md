This repository contains API Test Automation built while learning Pytest, REST API Testing, Test Automatization and basic framework structure.

This structure includes:
- Pytest-based test execution,
- Environment variable management,
- Modular test and utility structure

# Project Structure

src/ > Core Framework and API Utilities
tests/ > Test Cases
reports/ > Test Execution Reports

----

Setup:

1.Create a virtual environment and install dependencies:
    
    pip install -r requirements.txt

2. Copy environment variables file:

   powershell
    Copy env.example.ps1 env.ps1

4. Fill in your credentials inside env.ps1

Run all Tests:
pytest

Run tests with a specific marker:
pytest -m **testmark** 



