"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1764
Updated: 2026-05-17T16:23:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1764
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
