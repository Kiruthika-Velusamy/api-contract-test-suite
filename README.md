# api-contract-test-suite

## Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python |
| Framework | pytest |
| HTTP | requests |
| Config | YAML |
| Test Data | JSON + data factory |
| Reporting | Allure |
| CI/CD | GitHub Actions |
| API Tool | Postman + Newman |
| Database | SQLite |

## How to Run


# All tests
pytest

# By category
pytest -m smoke
pytest -m regression
pytest -m crud
pytest -m database

# Postman via Newman
newman run postman/collection.json \
  -e postman/environment.json

# Generate Allure report
allure serve reports/allure-results



## Author
Kiruthika Velusamy | QA Automation Engineer
[GitHub](https://github.com/Kiruthika-Velusamy)