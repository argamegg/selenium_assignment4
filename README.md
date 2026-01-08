# Selenium Assignment 4 (Amazon) - Bezhanov Arman, SE-2331

This project was created as part of **Assignment 4 – Practice with Advanced Selenium WebDriver**.
The goal of the assignment is to demonstrate practical usage of advanced Selenium features:
different waiting strategies, ActionChains, Select class, and test reporting.

All tests are implemented using **Python**, **Selenium WebDriver**, and **Pytest**.
The **Amazon** website was selected because it provides stable and real HTML elements
that work correctly with Selenium (including a native `<select>` element).

---

## Tested Website

https://www.amazon.com

---

## Project Structure

```text
selenium_assignment4/
├─ requirements.txt
├─ pytest.ini
├─ README.md
├─ reports/
│  └─ report.html
├─ src/
│  ├─ driver_factory.py
│  ├─ waits.py
│  └─ amazon_pages.py
└─ tests/
   ├─ conftest.py
   ├─ test_01_waits.py
   ├─ test_02_actions.py
   └─ test_03_select.py
```

---

## Description of Implemented Tests

### Test 01 – Wait Strategies (`test_01_waits.py`)

This test demonstrates different Selenium waiting mechanisms used to work with
dynamic web content on the Amazon search results page.

The following waiting strategies are implemented:

- **Implicit wait** – configured globally in the WebDriver.
- **Explicit wait** – used to wait for specific elements or conditions.
- **Fluent wait** – used with polling and ignored exceptions until product cards appear.

---

### Test 02 – ActionChains (`test_02_actions.py`)

This test demonstrates user interaction using **Selenium ActionChains**.

Actions performed:
- Move mouse to search input
- Click, clear input, type text
- Press Enter to submit search

The test verifies that the search is executed successfully.

---

### Test 03 – Select Class (`test_03_select.py`)

This test demonstrates working with a real HTML `<select>` element using
the Selenium **Select** class.

Steps:
- Locate sorting dropdown
- Change sorting option
- Verify selected option

---

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate    # macOS / Linux
# .venv\Scripts\activate     # Windows
python3 -m pip install -r requirements.txt
```

---

## Running Tests and Generating HTML Report

```bash
python3 -m pytest -v --html=reports/report.html --self-contained-html
```

---

## Headless Mode

```bash
HEADLESS=1 python3 -m pytest -v --html=reports/report.html --self-contained-html
```
