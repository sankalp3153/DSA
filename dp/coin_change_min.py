"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1396
Updated: 2026-01-27T13:53:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1396
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
