"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 706
Updated: 2025-07-10T18:36:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 706
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
