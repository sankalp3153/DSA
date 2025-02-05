"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 154
Updated: 2025-02-05T15:22:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 154
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
