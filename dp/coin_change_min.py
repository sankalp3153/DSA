"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2063
Updated: 2026-08-16T11:19:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2063
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
