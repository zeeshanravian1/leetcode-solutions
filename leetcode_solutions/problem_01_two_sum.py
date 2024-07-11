"""
# 1. Two Sum

URL:
    - https://leetcode.com/problems/two-sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of
the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

#### Example 1:

**Input:** nums = [2,7,11,15], target = 9

**Output:** [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

#### Example 2:

**Input:** nums = [3,2,4], target = 6

**Output:** [1,2]

#### Example 3:

**Input:** nums = [3,3], target = 6

**Output:** [0,1]

#### Constraints:

- $2 <= nums.length <= 10^4$
- $-10^9 <= nums[i] <= 10^9$
- $-10^9 <= target <= 10^9$
- **Only one valid answer exists.**

Follow-up: Can you come up with an algorithm that is less than 𝑂(𝑛2) time
complexity?

## **Solution:**

#### Intuition
The problem requires finding two indices in a list such that the sum of the
elements at these indices equals a given target. A brute force approach would
involve checking all pairs of indices, but this would be inefficient. Instead,
a more efficient solution can be achieved using a hash map (dictionary) to
store and quickly look up the indices of previously seen numbers.

#### Approach
- **Initialize a Hash Map (Dictionary):**

    Create an empty dictionary called
    seen to store numbers and their corresponding indices as you iterate
    through the list.

- **Iterate through the List:**

    For each number in the list, calculate its
    complement with respect to the target (i.e., target - num).

- **Check for Complement:**
    - If the complement is already in the dictionary, it means a pair of
    numbers that add up to the target has been found. Return the indices of the
    current number and its complement.

    - If the complement is not found, store the current number and its index
    in the dictionary.

- **Return Result:**

    If no such pair is found by the end of the iteration,
    return an empty list (though the problem guarantees exactly one solution,
    so this return is more of a safeguard).

#### Complexity
- **Time complexity:**

    The time complexity of this approach is **𝑂(𝑛)**, where **𝑛** is the number
    of elements in the list. This is because we iterate through the list once,
    and each dictionary operation (insertion and lookup) is **𝑂(1)** on average
    .

- **Space complexity:**

    The space complexity is **𝑂(𝑛)** because, in the worst case, we might store
    all **𝑛** elements in the dictionary if no two elements sum up to the
    target until the end.

"""


class Solution:
    """
    Solution Class

    Description:
        - This class solve the Two Sum problem by finding two indices in a list
        that add up to a specified target.

    Attributes:
        - `None`

    Methods:
        - `twoSum(nums: list[int], target: int) -> list[int]:` Finds two
        indices in `nums` that add up to `target`.

    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Two Sum Method

        Description:
            - This method finds two indices in `nums` that add up to `target`.

        Args:
            - `nums (list[int]):` A list of integers.
            - `target (int):` The target sum to find.

        Returns:
            - `list[int]:` A list of two indices that add up to `target`.

        """
        seen: dict[int, int] = {}

        for idx, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], idx]

            seen[num] = idx

        return []
