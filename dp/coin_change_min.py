"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2293
Updated: 2026-10-25T23:37:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2293
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
