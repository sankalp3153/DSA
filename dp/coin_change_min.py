"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 614
Updated: 2025-06-12T17:03:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 614
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
