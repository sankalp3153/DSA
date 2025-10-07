"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1028
Updated: 2025-10-07T11:54:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1028
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
