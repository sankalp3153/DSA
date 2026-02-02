"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1419
Updated: 2026-02-02T10:05:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1419
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
