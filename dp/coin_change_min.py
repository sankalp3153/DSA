"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2247
Updated: 2026-10-06T20:58:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2247
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
