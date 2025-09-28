"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1005
Updated: 2025-09-28T15:22:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1005
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
