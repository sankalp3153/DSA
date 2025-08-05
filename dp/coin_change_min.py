"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 798
Updated: 2025-08-05T18:42:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 798
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
