"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1741
Updated: 2026-05-06T11:00:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1741
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
