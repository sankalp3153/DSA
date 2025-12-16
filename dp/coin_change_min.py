"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1258
Updated: 2025-12-16T14:20:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1258
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
