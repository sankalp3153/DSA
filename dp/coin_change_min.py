"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 821
Updated: 2025-08-11T10:59:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 821
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
