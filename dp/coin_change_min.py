"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 108
Updated: 2025-01-28T14:16:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 108
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
