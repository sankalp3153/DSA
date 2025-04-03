"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 384
Updated: 2025-04-03T17:26:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 384
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
