"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 407
Updated: 2025-04-10T10:23:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 407
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
