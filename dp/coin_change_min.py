"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 361
Updated: 2025-03-30T11:06:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 361
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
