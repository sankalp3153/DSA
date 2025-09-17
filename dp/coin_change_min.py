"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 959
Updated: 2025-09-17T15:07:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 959
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
