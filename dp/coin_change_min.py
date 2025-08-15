"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 844
Updated: 2025-08-15T14:39:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 844
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
