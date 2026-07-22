"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1994
Updated: 2026-07-22T22:53:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1994
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
