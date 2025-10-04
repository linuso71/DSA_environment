import json
import pathlib

def solve(nums: list[int]) -> list[int]:
    """
    Leaders in an Array
    172
    100Medium

    Given an integer array nums, return a list of all the leaders in the array.

    A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.

    Examples:

    Input: nums = [1, 2, 5, 3, 1, 2]

    Output: [5, 3, 2]

    Explanation:

    2 is the rightmost element, 3 is the largest element in the index range [3, 5], 5 is the largest element in the index range [2, 5]

    This function identifies all 'leaders' in a given integer array. A leader is an element that is strictly
    greater than all elements to its right. The rightmost element is always considered a leader.

    Args:
        nums (list[int]): The input list of integers.

    Returns:
        list[int]: A list containing all the leaders in the order they appear in the input array.
    """
    pass


if __name__ == "__main__":
    category = "array"
    # Determine the path to the test file dynamically
    current_file_path = pathlib.Path(__file__).resolve()
    test_file_path = current_file_path.parent.parent / "testcases" / category / f"{current_file_path.stem}.json"

    if not test_file_path.exists():
        print(f"Error: Test file not found at {test_file_path}")
        exit(1)

    try:
        with open(test_file_path, 'r') as f:
            test_cases = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {test_file_path}")
        exit(1)
    except Exception as e:
        print(f"Error loading test cases: {e}")
        exit(1)

    total_tests = len(test_cases)
    passed_tests = 0

    for i, test_case in enumerate(test_cases):
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]

        # Assuming 'nums' is the only parameter based on the problem description
        nums = input_data["nums"]

        try:
            actual_output = solve(nums)
            if actual_output == expected_output:
                print(f"Test {i + 1}/{total_tests} Passed")
                passed_tests += 1
            else:
                print(f"Test {i + 1}/{total_tests} Failed")
                print(f"  Input: nums={nums}")
                print(f"  Expected: {expected_output}")
                print(f"  Actual: {actual_output}")
        except Exception as e:
            print(f"Test {i + 1}/{total_tests} Failed (Runtime Error)")
            print(f"  Input: nums={nums}")
            print(f"  Error: {e}")

    print(f"\n{'-'*30}")
    print(f"Summary: {passed_tests}/{total_tests} tests passed.")
    print(f"{'-'*30}")
