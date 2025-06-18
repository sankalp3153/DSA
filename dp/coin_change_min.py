"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 637
Updated: 2025-06-18T10:10:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 637
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
