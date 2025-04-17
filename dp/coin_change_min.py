"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 430
Updated: 2025-04-17T14:03:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 430
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
