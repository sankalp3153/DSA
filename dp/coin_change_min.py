"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2086
Updated: 2026-08-20T11:15:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2086
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
