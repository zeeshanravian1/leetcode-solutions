"""
# 1. Add Two Numbers

URL:
    - https://leetcode.com/problems/add-two-numbers

## Problem Statement

You are given two **non-empty** linked lists representing two non-negative
integers. The digits are stored in **reverse order**, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

#### Example 1:

![image.png](attachment:image.png)

**Input:** l1 = [2,4,3], l2 = [5,6,4]

**Output:** [7,0,8]

**Explanation:** 342 + 465 = 807.

#### Example 2:

**Input:** l1 = [0], l2 = [0]

**Output:** [0]

#### Example 3:

**Input:** l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]

**Output:** [8,9,9,9,0,0,0,1]

#### Constraints:

- The number of nodes in each linked list is in the range $[1, 100]$.
- $0 <= Node.val <= 9$
- **It is guaranteed that the list represents a number that does not have**
**leading zeros.**

## **Solution:**

#### Intuition
My initial approach leverages the convenience of the numbers being stored in
reverse order. This setup allows us to add corresponding digits
straightforwardly, similar to hand addition from the least to the most
significant digits. Managing the carry from one digit to the next is crucial,
particularly when one list is shorter than the other or when the final sum
results in an extra carry that extends the length of the resulting number.
The straightforward traversal of both lists with a dummy node to handle the
head of the result list efficiently handles these challenges and edge cases.

#### Approach
- **Initialization:**

    Start with a dummy head node which helps in easily returning the resulting
    linked list without needing extra condition checks.

- **Traversal and Summation:**

    Traverse both linked lists simultaneously, summing the corresponding digits
    and the carry from the previous iteration. If one list is shorter, treat
    missing digits as zero.

- **Carry Handling:**

    After adding two digits and the carry, compute the new digit to store in
    the result list (using modulus 10) and update the carry for the next
    iteration (using integer division by 10).

- **Next Node Creation:**

    Append the resultant digit as a new node to the result linked list.

- **Advance Pointers:**

    Move pointers forward in both input lists if nodes are available.

- **Final Check for Carry:**

    After processing both lists, if there's any remaining carry, append it as a
    new node to the result list.

- **Return the Result:**

    The result list starts from the node next to the dummy head.

#### Complexity
- **Time complexity:**

    The algorithm traverses each node of both linked lists exactly once. Hence,
    the time complexity is **𝑂(𝑛+𝑚)**, where **𝑛** and **𝑚** are the lengths
    of the two linked lists respectively.

- **Space complexity:**

    The space complexity is **𝑂(max⁡(𝑛,𝑚))**, primarily due to the space needed
    for the new linked list storing the sum of the two numbers. In the worst
    case, the length of the resultant list is **𝑂(max(𝑛,𝑚)+1)** (if there's a
    carry that extends the length).

"""


# Definition for singly-linked list.
class ListNode:
    """
    ListNode Class

    Description:
        - This class represents a node in a linked list.

    Attributes:
        - `val (int):` The value stored in the node.
        - `next (ListNode | None):` The next node in the linked list.

    Methods:
        - `None`

    """

    def __init__(self, val=0, next=None) -> None:
        """
        Initialization Method

        Description:
            - This method initializes the properties of the ListNode class.

        Args:
            - `val (int):` The value stored in the node.
            - `next (ListNode | None):` The next node in the linked list.

        Returns:
            - `None`

        """

        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    """
    Solution Class

    Description:
        - This class solve the Two Sum problem by finding two indices in a list
        that add up to a specified target.

    Attributes:
        - `None`

    Methods:
        - `addTwoNumbers(l1: ListNode | None, l2: ListNode | None):` Adds two
        linked lists.

    """

    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        """
        Add Two Numbers Method

        Description:
            - This method adds two linked lists.

        Args:
            - `l1 (ListNode | None):` The first linked list.
            - `l2 (ListNode | None):` The second linked list.

        Returns:
            - `ListNode | None`: The result linked list.

        """

        if not l1:
            return l2
        if not l2:
            return l1

        carry: int = 0
        head: ListNode = ListNode()
        current: ListNode = head

        while l1 or l2 or carry:
            val1: int = l1.val if l1 else 0
            val2: int = l2.val if l2 else 0

            val_sum: int = val1 + val2 + carry
            carry = val_sum // 10

            current.next = ListNode(val_sum % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
