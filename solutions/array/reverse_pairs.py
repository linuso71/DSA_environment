import json
import pathlib
from typing import List


def solve(nums: List[int]) -> int:
    """
    https://leetcode.com/problems/reverse-pairs/description/

    Given an integer array `nums`, return the number of *reverse pairs* in the array.

    A reverse pair is a pair `(i, j)` where `0 <= i < j < nums.length` and `nums[i] > 2 * nums[j]`.

    Constraints:
    - `1 <= nums.length <= 5 * 10^4`
    - `-2 * 10^9 <= nums[i] <= 2 * 10^9`

    :param nums: The input integer array.
    :return: The number of reverse pairs in the array.
    """
    pass


if __name__ == "__main__":
    problem_name = "reverse_pairs"
    # Determine the category based on the problem (e.g., array, string, etc.)
    # This needs to be set manually or derived from a separate mapping.
    # For this specific problem, it's categorized as 'array'.
    category = "array"

    # Construct the path to the test file
    current_dir = pathlib.Path(__file__).parent
    test_file_path = current_dir.parent.parent / "testcases" / category / f"{problem_name}.json"

    if not test_file_path.exists():
        print(f"Error: Test file not found at {test_file_path}")
        exit(1)

    with open(test_file_path, "r") as f:
        test_cases = json.load(f)

    num_passed = 0
    num_failed = 0

    for i, test_case in enumerate(test_cases):
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]

        # Assuming 'solve' function takes parameters matching keys in input_data
        # For 'reverse_pairs', input_data has one key: 'nums'
        try:
            actual_output = solve(**input_data)

            if actual_output == expected_output:
                print(f"Test {i + 1}: Passed")
                num_passed += 1
            else:
                print(f"Test {i + 1}: Failed")
                print(f"  Input: {input_data}")
                print(f"  Expected: {expected_output}")
                print(f"  Got: {actual_output}")
                num_failed += 1
        except Exception as e:
            print(f"Test {i + 1}: Error during execution")
            print(f"  Input: {input_data}")
            print(f"  Error: {e}")
            num_failed += 1

    print(f"\nSummary: {num_passed} tests passed, {num_failed} tests failed.")
