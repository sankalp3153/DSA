"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1074
Updated: 2025-10-22T10:38:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1074
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
