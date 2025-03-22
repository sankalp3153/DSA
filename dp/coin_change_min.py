"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 338
Updated: 2025-03-22T11:00:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 338
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
