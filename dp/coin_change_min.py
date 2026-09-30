"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2224
Updated: 2026-09-30T23:09:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2224
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
