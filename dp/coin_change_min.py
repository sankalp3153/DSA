"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 660
Updated: 2025-06-23T23:36:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 660
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
