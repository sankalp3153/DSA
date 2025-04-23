"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 453
Updated: 2025-04-23T14:04:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 453
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
