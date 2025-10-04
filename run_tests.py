import os
import sys
import json
import importlib.util
import argparse
import time

# --- Configuration ---
SOLUTIONS_DIR = "solutions"
TESTCASES_DIR = "testcases"

# --- ANSI Color Codes for Terminal Output ---
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'

def run_tests(problem_filename):
    """
    Dynamically imports a solution module, loads its corresponding test cases,
    and runs them, reporting the results.
    """
    solution_path = os.path.join(SOLUTIONS_DIR, f"{problem_filename}.py")
    testcase_path = os.path.join(TESTCASES_DIR, f"{problem_filename}.json")

    # --- Validate file existence ---
    if not os.path.exists(solution_path):
        print(f"{Colors.RED}Error: Solution file not found at '{solution_path}'{Colors.ENDC}")
        sys.exit(1)
    if not os.path.exists(testcase_path):
        print(f"{Colors.RED}Error: Test case file not found at '{testcase_path}'{Colors.ENDC}")
        sys.exit(1)

    # --- Dynamically import the solution module ---
    try:
        spec = importlib.util.spec_from_file_location(problem_filename, solution_path)
        solution_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(solution_module)
        solve_function = solution_module.solve
    except Exception as e:
        print(f"{Colors.RED}Error importing solution module or finding 'solve' function: {e}{Colors.ENDC}")
        sys.exit(1)

    # --- Load test cases ---
    try:
        with open(testcase_path, 'r') as f:
            test_cases = json.load(f)
    except json.JSONDecodeError as e:
        print(f"{Colors.RED}Error reading or parsing test case file '{testcase_path}': {e}{Colors.ENDC}")
        sys.exit(1)

    # --- Run tests ---
    passed_count = 0
    total_count = len(test_cases)
    print(f"{Colors.BLUE}--- Running tests for {problem_filename} ---{Colors.ENDC}\n")

    for i, test in enumerate(test_cases):
        inputs = test["input"]
        expected = test["expected_output"]

        start_time = time.perf_counter()
        actual = None
        try:
            # DYNAMIC INPUT HANDLING:
            # If input is a dictionary, unpack as keyword arguments (**kwargs).
            # If input is a list, unpack as positional arguments (*args).
            if isinstance(inputs, dict):
                actual = solve_function(**inputs)
            elif isinstance(inputs, list):
                actual = solve_function(*inputs)
            else:
                raise TypeError(f"Test case input must be a dictionary or a list, but got {type(inputs)}")

            end_time = time.perf_counter()
            duration_ms = (end_time - start_time) * 1000

            if actual == expected:
                passed_count += 1
                print(f"{Colors.GREEN}✅ Test Case {i + 1}: PASSED{Colors.ENDC} ({duration_ms:.2f} ms)")
            else:
                print(f"{Colors.RED}❌ Test Case {i + 1}: FAILED{Colors.ENDC} ({duration_ms:.2f} ms)")
                print(f"   - Input:    {inputs}")
                print(f"   - Expected: {expected}")
                print(f"   - Got:      {actual}")
        except Exception as e:
            end_time = time.perf_counter()
            duration_ms = (end_time - start_time) * 1000
            print(f"{Colors.RED}❌ Test Case {i + 1}: ERROR{Colors.ENDC} ({duration_ms:.2f} ms)")
            print(f"   - An exception occurred during execution: {e}")

    # --- Print Summary ---
    print("\n--- Summary ---")
    color = Colors.GREEN if passed_count == total_count else Colors.YELLOW
    print(f"{color}Passed {passed_count}/{total_count} test cases.{Colors.ENDC}")

    if passed_count != total_count:
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run test cases for a specific DSA solution."
    )
    parser.add_argument(
        "problem_filename",
        type=str,
        help="The base filename of the problem to test (e.g., 'two_sum')."
    )
    args = parser.parse_args()
    run_tests(args.problem_filename)

