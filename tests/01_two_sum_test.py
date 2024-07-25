"""
01. Two Sum Test Module

Description:
    - This module contains test cases for the two sum problem.

"""

from typing import Any

import pytest

from leetcode_solutions.problem_01_two_sum import Solution


class TestTwoSum:
    """
    TestTwoSum Class

    Description:
        - This class contains test cases for the Solution class's twoSum
        method.

    Attributes:
        - `test_cases (List[Dict[str, Any]]):` A list of test cases with input
        data and expected output.

    Methods:
        - `run_tests() -> None:` Runs test cases to validate the solution.

    """

    test_cases: list[dict[str, Any]] = [
        {
            "nums": [2, 7, 11, 15],
            "target": 9,
            "expected_output": [0, 1],
        },
        {
            "nums": [3, 2, 4],
            "target": 6,
            "expected_output": [1, 2],
        },
        {
            "nums": [3, 3],
            "target": 6,
            "expected_output": [0, 1],
        },
    ]

    @pytest.mark.parametrize("case", test_cases)
    def test_two_sum(self, case: dict[str, Any]) -> None:
        """
        Test Two Sum Method

        Description:
            - This method tests the twoSum method of the Solution class.

        Args:
            - `case (Dict[str, Any]):` A dictionary containing input data and
            expected output.

        Asserts:
            - Asserts that the output from twoSum method matches the expected
            output.

        """
        solution = Solution()
        assert (
            solution.twoSum(case["nums"], case["target"])
            == case["expected_output"]
        )
