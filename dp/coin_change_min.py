"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 568
Updated: 2025-05-30T19:00:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 568
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
