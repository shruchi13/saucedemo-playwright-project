# saucedemo-playwright-project
# SauceDemo E-Commerce Test Automation Framework

![Playwright](https://img.shields.io/badge/Playwright-1.40+-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Behave](https://img.shields.io/badge/Behave-BDD-222222?style=for-the-badge&logo=gherkin&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

An end-to-end BDD (Behavior-Driven Development) test automation framework built with **Python**, **Playwright**, and **Behave**. This project automates core user workflows on the [SauceDemo](https://www.saucedemo.com/) e-commerce web application, featuring clean **Page Object Model (POM)** architecture, custom HTML reporting, and automated **GitHub Actions CI/CD pipelines** for smoke and regression testing.

---

## Key Features

- **BDD Framework:** Human-readable Gherkin scenarios powered by Python Behave.
- **Page Object Model (POM):** Scalable and maintainable design pattern separating UI selectors and interactions from step definitions.
- **Cross-Environment Execution:** Automatic headless mode handling in CI/CD environments and customizable browser launch options.
- **Suite Tagging:** Flexible execution targeting high-priority `@smoke` tests vs. full `@regression` suites.
- **CI/CD Integration:** Automated workflow runs on GitHub Actions triggered by Pull Requests and daily scheduled cron jobs.
- **Rich HTML Reporting:** Self-contained, downloadable HTML test execution reports generated using `behave-html-formatter`.

---

## Project Structure

```text
saucedemo-playwright-project/
├── .github/
│   └── workflows/
│       ├── smoke-tests.yml        # CI pipeline: Runs @smoke on PRs and main commits
│       └── regression-tests.yml   # CI pipeline: Scheduled daily @regression runs
├── features/
│   ├── environment.py             # Behave hooks (browser launch/teardown, CI setup)
│   ├── steps/
│   │   ├── auth_steps.py          # Step definitions for authentication
│   │   ├── checkout_steps.py      # Step definitions for checkout flow
│   │   └── inventory_steps.py     # Step definitions for product list
│   ├── checkout.feature           # Gherkin scenarios for checkout
│   └── login.feature              # Gherkin scenarios for login
├── pages/                         # Page Object Model layer
│   ├── base_page.py               # Shared browser helper methods
│   ├── checkout_page.py           # Selectors & interactions for checkout pages
│   ├── inventory_page.py          # Selectors & interactions for product listing
│   └── login_page.py              # Selectors & interactions for login page
├── reports/                       # Generated test execution reports
├── behave.ini                     # Behave framework configuration settings
├── requirements.txt               # Python package dependencies
└── README.md                      # Project documentation
