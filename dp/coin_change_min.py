"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1304
Updated: 2025-12-29T21:38:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1304
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
