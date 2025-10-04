import json
import pathlib

def solve(sorted_numbers: list[int], target_value: int) -> list[int]:
    """
    First and last occurrence
114
100Easy

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If the target is not found in the array, return [-1, -1].
Examples:

Input: nums = [5, 7, 7, 8, 8, 10], target = 8

Output: [3, 4]

Explanation:The target is 8, and it appears in the array at indices 3 and 4, so the output is [3,4]

    Finds the starting and ending position of a given target value in a sorted array.

    Args:
        sorted_numbers: A list of integers sorted in non-decreasing order.
        target_value: The integer value to search for.

    Returns:
        A list of two integers, [start_index, end_index], representing the first and last
        occurrence of the target. Returns [-1, -1] if the target is not found.
    """
    pass

if __name__ == "__main__":
    PROBLEM_CATEGORY = "binary_search"
    
    problem_filename_stem = pathlib.Path(__file__).stem

    test_file_path = pathlib.Path(__file__).parent.parent / "testcases" / PROBLEM_CATEGORY / f"{problem_filename_stem}.json"

    print(f"Looking for test cases at: {test_file_path}")

    try:
        with open(test_file_path, 'r') as f:
            test_cases = json.load(f)
    except FileNotFoundError:
        print(f"Error: Test file not found at {test_file_path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {test_file_path}. Check file format.")
        exit(1)

    all_passed = True
    for i, test_case in enumerate(test_cases):
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]

        nums_param = input_data["sorted_numbers"]
        target_param = input_data["target_value"]

        actual_output = solve(nums_param, target_param)

        if actual_output == expected_output:
            print(f"Test Case {i+1} Passed: Input={input_data}, Expected={expected_output}, Got={actual_output}")
        else:
            print(f"Test Case {i+1} Failed: Input={input_data}, Expected={expected_output}, Got={actual_output}")
            all_passed = False

    if all_passed:
        print("\nAll test cases passed!")
    else:
        print("\nSome test cases failed.")
