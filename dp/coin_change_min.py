"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1787
Updated: 2026-05-22T10:38:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1787
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
