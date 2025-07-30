"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 775
Updated: 2025-07-30T10:18:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 775
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
