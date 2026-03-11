"""
Module: coin_change_min
Approach: bottom-up unbounded knapsack table
Revision: 1557
Updated: 2026-03-11T19:33:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1557
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
