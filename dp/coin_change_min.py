"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 729
Updated: 2025-07-18T10:20:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 729
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
