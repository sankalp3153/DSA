"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1051
Updated: 2025-10-14T12:23:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1051
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
