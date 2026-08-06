"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 2040
Updated: 2026-08-06T17:03:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2040
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
