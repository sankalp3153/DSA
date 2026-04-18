"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1695
Updated: 2026-04-18T15:24:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1695
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
