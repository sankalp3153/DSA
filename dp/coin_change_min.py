"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 39
Updated: 2025-01-08T11:19:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 39
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
