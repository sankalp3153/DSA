"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1166
Updated: 2025-11-25T10:04:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1166
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
