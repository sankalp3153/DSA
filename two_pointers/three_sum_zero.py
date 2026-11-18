"""
Three Sum (a + b + c == 0) with sorted duplicate-skipping two pointers.
Time: O(n^2) | Space: O(1) auxiliary
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums_sorted = sorted(nums)
    n = len(nums_sorted)
    triplets: List[List[int]] = []

    for i in range(n - 2):
        if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
            continue
        if nums_sorted[i] > 0:
            break

        left, right = i + 1, n - 1
        while left < right:
            total = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
            if total == 0:
                triplets.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                left += 1
                right -= 1
                while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                    left += 1
                while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return triplets
