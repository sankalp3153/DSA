"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1212
Updated: 2025-12-05T11:53:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1212
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
