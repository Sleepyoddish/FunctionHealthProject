# Function Health - Booking and Payment Flow Automation

## Overview

This repository contains automated tests for the Ezra/Function Health booking flow. The project uses **Playwright with Python** and implements a **Page Object Model (POM)** structure to ensure scalability and maintainability.  

The tests focus on the top-priority booking flow scenarios, including login, scan selection, appointment scheduling, and payment confirmation.

---

## Project Structure

FunctionHealthProject/
│
├─ pages/ # Page Object Model classes
│ ├─ login_page.py
│ ├─ scan_page.py
│ ├─ booking_page.py
│ └─ payment_page.py
│
├─ tests/ # Test cases
│ ├─ test_successful_booking_flow.py
│ └─ ... other tests
│
├─ conftest.py # Pytest fixtures
├─ requirements.txt # Python dependencies
└─ README.md


---

## Setup Instructions

1. Clone the repository:

```bash
git clone <your-repo-url>
cd FunctionHealthProject

2. Create a virtual environment and activate it:

python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

3. Install the required dependencies:

```bash
pip install -r requirements.txt

Run tests in headed mode:
pytest tests/test_successful_booking_flow.py --headed
pytest tests/ --headed # Run all tests in headed mode
```

Trade-offs and Assumptions

Assumptions:

-Test users exist in the staging environment.

-Payment flows use Stripe test cards.

-The booking flow is deterministic; network delays and dynamic data may cause occasional flakiness.


Trade-offs:

-Using UI element assertions for payment confirmation rather than strict URL checks. Stripe appends dynamic query parameters, which makes URL-based verification unreliable.

-Limited test coverage of edge cases for inaccessible back-end data (no DB or API-level assertions).
 

Scalability and Maintainability

-Page Object Model (POM): Each page interaction is encapsulated in its own class, making it easy to update locators and methods without affecting test logic.
-Fixtures: Common setup and teardown logic is handled via pytest fixtures in conftest.py, promoting code reuse.

Future improvements:

-Include API-level validation for sensitive data flows.

-Add retries or resilience for flaky elements like dynamic iframes.

-Implement data-driven tests for broader coverage of input scenarios.

-Enhance logging and reporting for better test result analysis.

-Make locators more versatile, robust, and stable by using more reliable selectors (e.g., data-testids).

-Expand test coverage to include negative scenarios and edge cases.

-Create more helper methods in page classes to reduce code duplication across tests.

-Integrate with CI/CD pipelines for automated test execution on code changes.

-Add cross-browser testing to ensure compatibility across different browsers.