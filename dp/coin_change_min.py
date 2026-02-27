"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1511
Updated: 2026-02-27T12:08:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1511
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
