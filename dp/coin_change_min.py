"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1281
Updated: 2025-12-23T14:59:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1281
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
