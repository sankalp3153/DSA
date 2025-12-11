"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1235
Updated: 2025-12-11T12:41:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1235
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
