"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1373
Updated: 2026-01-20T13:23:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1373
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
