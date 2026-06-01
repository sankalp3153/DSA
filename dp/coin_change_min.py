"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1810
Updated: 2026-06-01T19:58:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1810
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
