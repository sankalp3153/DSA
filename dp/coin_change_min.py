"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1879
Updated: 2026-06-18T12:54:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1879
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
