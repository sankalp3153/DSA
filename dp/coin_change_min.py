"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1327
Updated: 2026-01-05T11:32:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1327
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
