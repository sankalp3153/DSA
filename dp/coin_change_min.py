"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 16
Updated: 2025-01-03T20:06:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 16
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
