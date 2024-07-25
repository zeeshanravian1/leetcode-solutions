"""
02. Add Two Numbers Test Module

Description:
    - This module contains test cases for the add two numbers problem.

"""

import pytest

from leetcode_solutions.problem_02_add_two_numbers import ListNode, Solution


class TestAddTwoNumbers:
    """
    TestAddTwoNumbers Class

    Description:
        - This class contains test cases for the Solution class's addTwoNumbers
        method.

    Attributes:
        - `test_cases (: list[dict[str, ListNode]]):` A list of test cases with
        input data and expected output.

    Methods:
        - `test_add_two_numbers(case: dict[str, Any]) -> None:` Runs a test
        case to validate the solution.

    """

    test_cases: list[dict[str, ListNode]] = [
        {
            "l1": ListNode(2, ListNode(4, ListNode(3))),
            "l2": ListNode(5, ListNode(6, ListNode(4))),
            "expected_output": ListNode(7, ListNode(0, ListNode(8))),
        },
        {
            "l1": ListNode(0),
            "l2": ListNode(0),
            "expected_output": ListNode(0),
        },
        {
            "l1": ListNode(
                9,
                ListNode(
                    9,
                    ListNode(
                        9,
                        ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
                    ),
                ),
            ),
            "l2": ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
            "expected_output": ListNode(
                8,
                ListNode(
                    9,
                    ListNode(
                        9,
                        ListNode(
                            9,
                            ListNode(0, ListNode(0, ListNode(0, ListNode(1)))),
                        ),
                    ),
                ),
            ),
        },
    ]

    @pytest.mark.parametrize("case", test_cases)
    def test_add_two_numbers(self, case: dict[str, ListNode]) -> None:
        """
        Test Add Two Numbers Method

        Description:
            - This method tests the addTwoNumbers method of the Solution class.

        Args:
            - `case (: list[dict[str, ListNode]]):` A dictionary containing
            input data and expected output.

        Asserts:
            - Asserts that the output from addTwoNumbers method matches the
            expected output.

        """

        def are_equal(l1: ListNode | None, l2: ListNode | None) -> bool:
            """
            Are Equal Method

            Description:
                - This method checks if two linked lists are equal.

            Args:
                - `l1 (ListNode | None):` The first linked list.
                - `l2 (ListNode | None):` The second linked list.

            Returns:
                - `bool`: True if the linked lists are equal, False otherwise.

            """
            while l1 and l2:
                if l1.val != l2.val:
                    return False
                l1 = l1.next
                l2 = l2.next
            return not l1 and not l2

        solution = Solution()
        assert are_equal(
            solution.addTwoNumbers(l1=case["l1"], l2=case["l2"]),
            case["expected_output"],
        )
