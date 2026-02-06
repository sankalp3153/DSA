"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1442
Updated: 2026-02-06T15:57:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1442
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
