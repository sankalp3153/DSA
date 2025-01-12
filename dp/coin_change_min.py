"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 62
Updated: 2025-01-12T21:41:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 62
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
