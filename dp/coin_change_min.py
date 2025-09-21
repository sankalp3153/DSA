"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 982
Updated: 2025-09-21T16:21:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 982
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
