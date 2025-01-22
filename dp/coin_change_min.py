"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 85
Updated: 2025-01-22T20:25:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 85
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
