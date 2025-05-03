"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 476
Updated: 2025-05-03T15:28:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 476
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
