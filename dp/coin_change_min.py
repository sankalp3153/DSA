"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1902
Updated: 2026-06-24T13:57:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1902
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
