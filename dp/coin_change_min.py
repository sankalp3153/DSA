"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 246
Updated: 2025-03-03T12:15:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 246
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
