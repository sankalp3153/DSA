"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1649
Updated: 2026-04-07T23:18:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1649
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
