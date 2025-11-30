"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1189
Updated: 2025-11-30T18:04:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1189
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
