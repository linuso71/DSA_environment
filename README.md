# DSA Generator & Test Runner

This repository contains two main tools for Data Structures & Algorithms (DSA) practice:

- **script.py**: Automatically scaffolds DSA problems using Gemini AI, generating solution boilerplate, test cases, and updating an Excel progress report.
- **run_tests.py**: Runs the generated test cases against your solution and reports results in the terminal.

---

## Features

### script.py

- **AI-powered scaffolding**: Generates Python solution templates and JSON test cases for any DSA problem description or URL.
- **Automatic categorization**: Organizes problems by category (array, string, tree, etc.).
- **Excel progress tracking**: Updates `dsa_progress_report.xlsx` with problem details, including title and description extracted from URLs.
---

## Setup

1. **Clone the repository**

   ```sh
   git clone https://github.com/yourusername/dsa-generator.git
   cd dsa-generator
   ```

2. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your Gemini API key**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

---

## Usage

### 1. Scaffold a new problem

You can provide a problem description or a URL (e.g., LeetCode link):

```sh
python script.py "https://leetcode.com/problems/two-sum/"
```

or

```sh
python script.py "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."
```

- This will generate:
  - A solution file in `solutions/<category>/<filename>.py`
  - A test case file in `testcases/<category>/<filename>.json`
  - An updated Excel report: `dsa_progress_report.xlsx`

### 2. Run tests for a solution

```sh
python run_tests.py <filename>
```

- Example:
  ```sh
  python run_tests.py two_sum
  ```
- This will run all test cases for `solutions/<category>/two_sum.py` and report results.

---

## Folder Structure

```
solutions/
  <category>/
    <filename>.py

testcases/
  <category>/
    <filename>.json

dsa_progress_report.xlsx
script.py
run_tests.py
.env
```

---

## Notes

- Make sure your `.env` file contains a valid Gemini API key.
- The Excel report will automatically update with each new problem.
- You can manually edit solution files to implement your logic and re-run tests anytime.

---

## License

MIT License
