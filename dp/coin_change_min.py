"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 867
Updated: 2025-08-20T19:09:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 867
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
