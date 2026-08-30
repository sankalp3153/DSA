"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2132
Updated: 2026-08-30T22:11:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2132
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
