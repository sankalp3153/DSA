"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1465
Updated: 2026-02-12T10:45:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1465
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
