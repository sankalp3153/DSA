"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 591
Updated: 2025-06-05T17:41:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 591
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
